from pathlib import Path
r=Path('outputs/Stratus/shaders'); c=r/'core'
(c/'temporal-optics.glsl').write_text('''#ifndef STRATUS_TEMPORAL_OPTICS_INCLUDED
#define STRATUS_TEMPORAL_OPTICS_INCLUDED
// Geometry hints only: no previous radiance, omitted occlusion search or
// accumulated colour. Every accepted hit is validated against current depth.
#if TEMPORAL_OPTICS == 1
uniform int frameCounter;
uniform float frameTime;
float previousOpticalHint(sampler2D history,ivec2 cell){
    if(frameCounter<=1||frameTime<=0.0||frameTime>0.05)return 0.0;
    vec2 value=texelFetch(history,cell,0).rg;
    return value.y==float((frameCounter-1)%1024)&&value.x>0.0?value.x:0.0;
}
vec2 nextOpticalHint(float value){return vec2(max(value,0.0),float(frameCounter%1024));}
#endif
#endif
''')
p=c/'options.glsl';s=p.read_text().replace('#define TEMPORAL_ATMOSPHERE 1 // [0 1]','#define TEMPORAL_ATMOSPHERE 1 // [0 1]\n#define TEMPORAL_OPTICS 1 // [0 1]');p.write_text(s)
p=c/'scene-trace.glsl';s=p.read_text()
# Validate one temporal plane candidate with all original tests, then retain
# the original search unchanged if it fails. Prefix traversal still runs.
start=s.index('    float sampleT=minimum+0.025;boundUV=')
s=s[:start]+s[start:].replace('    float sampleT=minimum+0.025;boundUV=', '    float sampleT=minimum+0.025;boundUV=',1)
s=s.replace('out vec3 boundNormal){','out vec3 boundNormal,float temporalDistance){',1)
s=s.replace('    for(int iteration=0;iteration<4;iteration++){\n        vec2 uv;', '''    for(int iteration=-1;iteration<4;iteration++){
        if(iteration<0){if(temporalDistance<=minimum||temporalDistance>=maximum)continue;sampleT=temporalDistance;}
        else if(iteration==0)sampleT=minimum+0.025;
        vec2 uv;''',1)
# A bad temporal seed must not terminate the original fresh search.
a=s.index('    for(int iteration=-1;');b=s.index('    return maximum;',a)
part=s[a:b].replace('break;', '{if(iteration<0)continue;break;}')
s=s[:a]+part+s[b:]
s=s.replace('float minimum,out float path){','float minimum,out float path,float temporalDistance){',1)
s=s.replace('maximum,boundUV,boundPoint,boundNormal);','maximum,boundUV,boundPoint,boundNormal,temporalDistance);',1)
s=s.replace('maximum,false,0.025,path);','maximum,false,0.025,path,0.0);',1)
pos=s.index('\n#endif',s.index('vec4 traceOpticalScene'))
s=s[:pos]+'''
vec4 traceOpticalSceneHint(vec3 origin,vec3 direction,vec3 interfaceNormal,int side,int quality,float maximum,out float path,float temporalDistance){
    return traceOpticalSegment(origin,direction,interfaceNormal,side,quality,maximum,false,0.025,path,temporalDistance);
}
'''+s[pos:];p.write_text(s)
p=c/'water-reflection.frag.glsl';s=p.read_text().replace('in vec2 rasterUV;','#include "/core/temporal-optics.glsl"\n#if TEMPORAL_OPTICS == 1\nuniform sampler2D colortex16;\n#endif\nin vec2 rasterUV;')
s=s.replace('/* RENDERTARGETS: 7 */','''#if TEMPORAL_OPTICS == 1
/* RENDERTARGETS: 7,16 */
layout(location=1)out vec2 reflectionHint;
#else
/* RENDERTARGETS: 7 */
#endif''')
s=s.replace('    waterReflection=vec4(0.0);','    waterReflection=vec4(0.0);\n#if TEMPORAL_OPTICS == 1\n    reflectionHint=nextOpticalHint(0.0);\n#endif',1)
s=s.replace('    vec4 traced=sceneryReflection(view+n*0.015,boundary.reflected,n,hitDistance);','''    float hint=0.0;
#if TEMPORAL_OPTICS == 1
    hint=previousOpticalHint(colortex16,ivec2(gl_FragCoord.xy));
#endif
    vec4 traced=traceOpticalSceneHint(view+n*0.015,boundary.reflected,n,1,REFLECTION_MODE,min(REFLECT_RANGE,max(16.0,far)),hitDistance,hint);
#if TEMPORAL_OPTICS == 1
    reflectionHint=nextOpticalHint(traced.a>0.0?hitDistance:0.0);
#endif''');p.write_text(s)
p=c/'refraction.glsl';s=p.read_text();s=s.replace('float surfaceDepth){','float surfaceDepth,float previousRejectedStep,out float rejectedStep){',1).replace('    vec2 distortion=', '    rejectedStep=0.0;\n    vec2 distortion=',1)
s=s.replace('    for(int i=1;i<=checks;i++){','''    int previous=int(previousRejectedStep);
    // A previous rejection is only a search-order hint. Probe that CURRENT
    // segment location first; every accepted ray still runs every guard.
    if(previous>=1&&previous<=checks){
        vec2 edge=mix(uv,shifted,float(previous)/float(checks));float d=texture(depthtex1,edge).r;
        if(d<0.999999&&-positionFromDepth(edge,d).z<surfaceDepth+0.03){rejectedStep=float(previous);return uv;}
    }
    for(int i=1;i<=checks;i++){''',1)
s=s.replace('if(d<0.999999&&-positionFromDepth(edge,d).z<surfaceDepth+0.03)return uv;','if(d<0.999999&&-positionFromDepth(edge,d).z<surfaceDepth+0.03){rejectedStep=float(i);return uv;}',1)
# Preserve the old callable contract used by native probes/other includes.
s=s.replace('\n#endif\n', '\n#endif\n',1)
s=s.replace('\n#endif\n', '\n#endif\n',1)
last=s.rindex('\n#endif');s=s[:last]+'''
vec2 legacyWaterRefractionUV(vec2 uv,vec3 nView,vec3 faceView,float thickness,float surfaceDepth){
    float rejected;return legacyWaterRefractionUV(uv,nView,faceView,thickness,surfaceDepth,0.0,rejected);
}
'''+s[last:];p.write_text(s)
p=c/'lake.frag.glsl';s=p.read_text().replace('in vec2 rasterUV;','#include "/core/temporal-optics.glsl"\n#if TEMPORAL_OPTICS == 1\nuniform sampler2D colortex18;\n#endif\nin vec2 rasterUV;')
s=s.replace('/* RENDERTARGETS: 12 */','''#if TEMPORAL_OPTICS == 1
/* RENDERTARGETS: 12,18 */
layout(location=1)out vec2 refractionHint;
#else
/* RENDERTARGETS: 12 */
#endif''')
s=s.replace('void main(){','void main(){\n#if TEMPORAL_OPTICS == 1\n    refractionHint=nextOpticalHint(0.0);\n#endif',1)
s=s.replace('        vec2 shifted=legacyWaterRefractionUV(rasterUV,nView,faceView,thickness,markedDepth.x);','''        float hint=0.0,rejected;
#if TEMPORAL_OPTICS == 1 && REFRACTION_QUALITY > 0
        hint=previousOpticalHint(colortex18,ivec2(gl_FragCoord.xy));
#endif
        vec2 shifted=legacyWaterRefractionUV(rasterUV,nView,faceView,thickness,markedDepth.x,hint,rejected);
#if TEMPORAL_OPTICS == 1
        refractionHint=nextOpticalHint(rejected);
#endif''');p.write_text(s)
p=c/'transparent-optics.glsl';s=p.read_text().replace('// One nearest', '''#include "/core/temporal-optics.glsl"
#if TEMPORAL_OPTICS == 1
uniform sampler2D colortex17;
vec2 solidOpticalHint;
#endif
// One nearest''')
s=s.replace('    if(TRANSPARENT_REFLECTIONS<=0.0', '''#if TEMPORAL_OPTICS == 1
    solidOpticalHint=nextOpticalHint(0.0);
#endif
    if(TRANSPARENT_REFLECTIONS<=0.0''',1)
s=s.replace('        float path;hit=traceOpticalScene(point+n*0.015,direction,n,1,REFLECTION_MODE,min(REFLECT_RANGE,max(16.0,far)),false,path);','''        float path,hint=0.0;
#if TEMPORAL_OPTICS == 1
        hint=previousOpticalHint(colortex17,ivec2(gl_FragCoord.xy));
#endif
        hit=traceOpticalSceneHint(point+n*0.015,direction,n,1,REFLECTION_MODE,min(REFLECT_RANGE,max(16.0,far)),path,hint);
#if TEMPORAL_OPTICS == 1
        solidOpticalHint=nextOpticalHint(hit.a>0.0?path:0.0);
#endif''');p.write_text(s)
p=c/'atmosphere-resolve.frag.glsl';s=p.read_text().replace('/* RENDERTARGETS: 3 */','''#if TEMPORAL_OPTICS == 1
/* RENDERTARGETS: 3,17 */
layout(location=1)out vec2 transparentHint;
#else
/* RENDERTARGETS: 3 */
#endif''').replace('    // The atmosphere producer', '''#if TEMPORAL_OPTICS == 1
    transparentHint=solidOpticalHint;
#endif
    // The atmosphere producer''',1);p.write_text(s)
p=c/'resolve.frag.glsl';s=p.read_text().replace('const int colortex15Format', '''#if TEMPORAL_OPTICS == 1
const int RG16F = 33327;
const int colortex16Format = RG16F;
const int colortex17Format = RG16F;
const int colortex18Format = RG16F;
const bool colortex16Clear = false;
const bool colortex17Clear = false;
const bool colortex18Clear = false;
#endif
const int colortex15Format''',1);p.write_text(s)
p=r/'shaders.properties';s=p.read_text().replace('REFLECT_RANGE TEMPORAL_ATMOSPHERE','REFLECT_RANGE TEMPORAL_ATMOSPHERE TEMPORAL_OPTICS').replace('REFLECT_LEVEL REFLECT_RANGE TEMPORAL_ATMOSPHERE','REFLECT_LEVEL REFLECT_RANGE TEMPORAL_ATMOSPHERE TEMPORAL_OPTICS')
s=s.replace('TEMPORAL_OPTICS TEMPORAL_OPTICS','TEMPORAL_OPTICS')
s=s.replace('ORIGINAL_DAMPNESS:0.00','ORIGINAL_DAMPNESS:0.00 TEMPORAL_OPTICS:1')
s+='''
# Temporal intersection hints follow each existing producer's exact resolution.
#if TEMPORAL_OPTICS == 1
#if REFLECTION_MODE == 2
size.buffer.colortex16=1.0 1.0
#else
size.buffer.colortex16=0.5 0.5
#endif
#if WATER_RENDER_QUALITY == 2
size.buffer.colortex18=1.0 1.0
#elif WATER_RENDER_QUALITY == 1
size.buffer.colortex18=0.5 0.5
#else
size.buffer.colortex18=0.35 0.35
#endif
#endif
''';p.write_text(s)
p=r/'lang/en_us.lang';s=p.read_text();s+='''
option.TEMPORAL_OPTICS=Temporal optics hints
option.TEMPORAL_OPTICS.comment=Previous-frame intersection hints guide water and glass reflection searches and water shoreline rejection. All hits, occlusion and colours are evaluated from current geometry at the selected quality; no colour history, trails or frame skipping. Cheap sky lookup, thin-glass refraction and the straight underwater exit remain fresh. Extra history storage can cost performance; compare On and Off.
value.TEMPORAL_OPTICS.0=Off
value.TEMPORAL_OPTICS.1=On
''';p.write_text(s)
