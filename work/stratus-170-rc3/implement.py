from pathlib import Path
p=Path('outputs/Stratus/shaders')
f=p/'core/options.glsl';s=f.read_text().replace('#define ATMOSPHERE_QUALITY 1 // [0 1 2]','#define ATMOSPHERE_QUALITY 1 // [0 1 2]\n#define TEMPORAL_ATMOSPHERE 1 // [0 1]');f.write_text(s)
f=p/'shaders.properties';s=f.read_text().replace('REFLECT_RANGE <empty>','REFLECT_RANGE TEMPORAL_ATMOSPHERE');s='\n'.join(l+' TEMPORAL_ATMOSPHERE:1' if l.startswith('profile.') else l for l in s.splitlines())+'\n';f.write_text(s)
f=p/'lang/en_us.lang';s=f.read_text()+'\noption.TEMPORAL_ATMOSPHERE=Temporal sky reuse\noption.TEMPORAL_ATMOSPHERE.comment=Reuses sky atmosphere for at most one frame only with a stationary camera and unchanged projection, time, weather and status. Moving views, terrain, water and invalid history are evaluated freshly at the selected quality. No frame skipping; may introduce one-frame cloud motion delay. Off evaluates every pixel freshly.\nvalue.TEMPORAL_ATMOSPHERE.0=Off\nvalue.TEMPORAL_ATMOSPHERE.1=On\n';f.write_text(s)
f=p/'core/raster.frag.glsl';s=f.read_text().replace('category>1.05&&category<1.5&&material!=4113','category>1.05&&category<1.5&&(material!=4113||gl_FrontFacing)');f.write_text(s)
f=p/'core/resolve.frag.glsl';s=f.read_text().replace('const int colortex11Format = RGBA16F;','const int colortex11Format = RGBA16F;\n#if TEMPORAL_ATMOSPHERE == 1\nconst bool colortex11Clear = false;\n#endif');f.write_text(s)
(p/'core/temporal-atmosphere.glsl').write_text('''#ifndef STRATUS_TEMPORAL_ATMOSPHERE
#define STRATUS_TEMPORAL_ATMOSPHERE
// History lives in the existing ping-pong atmosphere target. Negative alpha
// marks sky, keeping terrain/water out of history without another depth buffer.
vec4 unpackAtmosphere(vec4 value){
#if TEMPORAL_ATMOSPHERE == 1
    if(value.a<0.0)value.a=-value.a-1.0;
#endif
    return value;
}
bool atmosphereHeader(ivec2 cell){
#if TEMPORAL_ATMOSPHERE == 1
    return cell.y==0&&cell.x<2;
#else
    return false;
#endif
}
#endif
''')
f=p/'core/atmosphere.frag.glsl';s=f.read_text().replace('in vec2 rasterUV;','''#include "/core/temporal-atmosphere.glsl"
#if TEMPORAL_ATMOSPHERE == 1
uniform sampler2D colortex11;
uniform int frameCounter;
uniform float frameTime;
uniform vec3 previousCameraPosition;
uniform mat4 gbufferPreviousModelView;
uniform mat4 gbufferPreviousProjection;
bool stableMatrix(mat4 a,mat4 b){
    return length(a[0]-b[0])+length(a[1]-b[1])+length(a[2]-b[2])+length(a[3]-b[3])<0.000001;
}
#endif
in vec2 rasterUV;''')
s=s.replace('float limit=sceneDistance', '''#if TEMPORAL_ATMOSPHERE == 1
    ivec2 cell=ivec2(gl_FragCoord.xy);
    float tick=mod(float(worldTime),24000.0);
    if(cell==ivec2(0,0)){integratedAtmosphere=vec4(float(frameCounter%1024),floor(tick/64.0),mod(tick,64.0),rainStrength);return;}
    if(cell==ivec2(1,0)){integratedAtmosphere=vec4(viewWidth,viewHeight,blindness,darknessFactor);return;}
#endif
    float limit=sceneDistance''')
s=s.replace('vec4 volume=completeAtmosphereSegment', '''#if TEMPORAL_ATMOSPHERE == 1
    // Only reuse the immediately preceding fresh odd frame, never a reuse chain.
    // Exact matrix equality deliberately rejects camera rotation, bob and FOV.
    if(frameCounter>1&&frameCounter%2==0&&limit>=6999.0&&frameTime>0.0&&frameTime<=0.05
       &&distance(cameraPosition,previousCameraPosition)<0.0001
       &&stableMatrix(gbufferModelView,gbufferPreviousModelView)
       &&stableMatrix(gbufferProjection,gbufferPreviousProjection)){
        vec4 header=texelFetch(colortex11,ivec2(0,0),0);
        vec4 state=texelFetch(colortex11,ivec2(1,0),0);
        bool valid=abs(header.x-float((frameCounter-1)%1024))<0.1
            &&header.y==floor(tick/64.0)&&header.z==mod(tick,64.0)
            &&abs(header.w-rainStrength)<0.00001
            &&state.xy==vec2(viewWidth,viewHeight)
            &&abs(state.z-blindness)<0.00001&&abs(state.w-darknessFactor)<0.00001;
        if(valid){vec4 history=texelFetch(colortex11,cell,0);if(history.a<=-1.0&&history.a>=-2.0){integratedAtmosphere=history;return;}}
    }
#endif
    vec4 volume=completeAtmosphereSegment''')
s=s.replace('integratedAtmosphere=vec4(volume.rgb*volume.a,volume.a);','''integratedAtmosphere=vec4(volume.rgb*volume.a,volume.a);
#if TEMPORAL_ATMOSPHERE == 1
    if(limit>=6999.0)integratedAtmosphere.a=-1.0-volume.a;
#endif''');f.write_text(s)
f=p/'core/atmosphere-resolve.frag.glsl';s=f.read_text().replace('#include "/core/transparent-optics.glsl"','#include "/core/transparent-optics.glsl"\n#include "/core/temporal-atmosphere.glsl"').replace('vec2 uv=(vec2(sampleCell)','if(atmosphereHeader(sampleCell))continue;\n        vec2 uv=(vec2(sampleCell)').replace('volume+=texelFetch(colortex11,sampleCell,0)*weight','volume+=unpackAtmosphere(texelFetch(colortex11,sampleCell,0))*weight');f.write_text(s)
