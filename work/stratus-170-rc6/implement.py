from pathlib import Path
import re
r=Path('outputs/Stratus/shaders');c=r/'core';old=Path('work/stratus-170-rc6/reference-131/shaders/core')
p=c/'options.glsl';s=p.read_text().replace('#define REFLECTION_MODE 0 // [0 1 2]','#define REFLECTION_MODE 0 // [0 1 2]\n#define REFLECTION_TRACE 0 // [0 1]')
assert '#define REFLECTION_TRACE' in s
s=s.replace('#define WET_SHEEN 0.85 //','#define WET_FILM_STYLE 0 // [0 1]\n#define WET_SHEEN 0.85 //');assert '#define WET_FILM_STYLE' in s;p.write_text(s)
# Restore the project's own1.3.1 bounded perspective-correct depth crossing
# implementation, retaining selected mode counts. Existing plane tracer remains.
s=(old/'trace.glsl').read_text();start=s.index('float screenDepthError');end=s.rindex('#endif');s=s[start:end]
s=s.replace('screenDepthError','classicScreenDepthError').replace('vec4 sceneryReflection(vec3 viewOrigin, vec3 viewDirection)', 'vec4 classicSceneryReflection(vec3 viewOrigin,vec3 viewDirection,vec3 interfaceNormal,int side,int quality,float maximum,out float path)')
s=s.replace('#if REFLECTION_MODE == 0\n    return vec4(0.0);\n#else\n','    path=0.0;\n')
s=s.replace('float distanceLimit = min(REFLECT_RANGE, max(16.0, far));','float distanceLimit = min(maximum,min(REFLECT_RANGE,max(16.0,far)));')
s=s.replace('#if REFLECTION_MODE == 2\n    const int count = 28;\n    const int bisections = 5;\n#else\n    const int count = 16;\n    const int bisections = 4;\n#endif','    int count=quality==2?28:16;\n    int bisections=quality==2?5:4;')
s=s.replace('            float missDistance =', '''            // Current medium-side protection remains even in the classic path.
            if(float(side)*dot(hitPoint-viewOrigin,interfaceNormal)<=0.005)return vec4(0.0);
            path=length(hitPoint-viewOrigin);
            float missDistance =''')
s=s.replace('\n#endif\n}', '\n}')
(c/'classic-reflection.glsl').write_text('#ifndef STRATUS_CLASSIC_REFLECTION_INCLUDED\n#define STRATUS_CLASSIC_REFLECTION_INCLUDED\n// Restored from this project\'s1.3.1 archive; no geometry/pixel-budget substitution.\n'+s+'\n#endif\n')
p=c/'scene-trace.glsl';s=p.read_text();pos=s.index('vec4 traceOpticalScene(');s=s[:pos]+'''#if REFLECTION_TRACE == 0
#include "/core/classic-reflection.glsl"
#endif
'''+s[pos:]
s=s.replace('    return traceOpticalSegment(origin,direction,interfaceNormal,side,quality,maximum,false,0.025,path,0.0);','''#if REFLECTION_TRACE == 0
    return classicSceneryReflection(origin,direction,interfaceNormal,side,quality,maximum,path);
#else
    return traceOpticalSegment(origin,direction,interfaceNormal,side,quality,maximum,false,0.025,path,0.0);
#endif''')
s=s.replace('    return traceOpticalSegment(origin,direction,interfaceNormal,side,quality,maximum,false,0.025,path,temporalDistance);','''#if REFLECTION_TRACE == 0
    return classicSceneryReflection(origin,direction,interfaceNormal,side,quality,maximum,path);
#else
    return traceOpticalSegment(origin,direction,interfaceNormal,side,quality,maximum,false,0.025,path,temporalDistance);
#endif''');p.write_text(s)
# Classic is the full old reflection cost/appearance, without the added
# per-hit20-step self-lit reflected mist. Detailed retains that complete path.
p=c/'water-reflection.frag.glsl';s=p.read_text().replace('    if(traced.a>0.0){','#if REFLECTION_TRACE == 1\n    if(traced.a>0.0){').replace('    waterReflection=vec4(traced.rgb*traced.a,traced.a);','#endif\n    waterReflection=vec4(traced.rgb*traced.a,traced.a);');p.write_text(s)
# Do not allocate/write unused geometry receiver normals for classic searches.
p=c/'resolve.frag.glsl';s=p.read_text().replace('const int colortex10Format = RGBA16F;','#if REFLECTION_TRACE == 1\nconst int colortex10Format = RGBA16F;\n#endif');s=s.replace('/* RENDERTARGETS: 3,4,0,1,2,8,10 */','''#if REFLECTION_TRACE == 1
/* RENDERTARGETS: 3,4,0,1,2,8,10 */
#else
/* RENDERTARGETS: 3,4,0,1,2,8 */
#endif''').replace('layout(location = 6) out vec4 opaqueReceiverNormal;','#if REFLECTION_TRACE == 1\nlayout(location = 6) out vec4 opaqueReceiverNormal;\n#endif').replace('    opaqueReceiverNormal=geometry?', '#if REFLECTION_TRACE == 1\n    opaqueReceiverNormal=geometry?').replace('    emptyWaterTint=vec4(0.0);','#endif\n    emptyWaterTint=vec4(0.0);');p.write_text(s)
# Geometry-only temporal seeds are unused in classic mode; shoreline hints
# remain independently available under their retained saved option.
for name in ['water-reflection.frag.glsl','transparent-optics.glsl','atmosphere-resolve.frag.glsl']:
 p=c/name;p.write_text(p.read_text().replace('#if TEMPORAL_OPTICS == 1 && REFLECTION_MODE != 0','#if TEMPORAL_OPTICS == 1 && REFLECTION_MODE != 0 && REFLECTION_TRACE == 1'))
p=c/'resolve.frag.glsl';p.write_text(p.read_text().replace('#if REFLECTION_MODE != 0\nconst int colortex16Format','#if REFLECTION_MODE != 0 && REFLECTION_TRACE == 1\nconst int colortex16Format'))
# Project1.3.1 dielectric/GGX film, decoupled from diffuse pore absorption and
# with the approved common roughness rather than material-class differences.
s=(old/'diffuse.glsl').read_text();helpers=s[s.index('float waterFresnel('):s.index('vec3 diffuseRadiance(')].replace('waterFresnel','classicWetFresnel').replace('wetSunSpecular','classicWetSunSpecular')
p=c/'diffuse.glsl';s=p.read_text();s=s.replace('vec3 wetSurfaceResponse(',helpers+'\nvec3 wetSurfaceResponse(',1)
a=s.index('    float filmSource=',s.index('vec3 wetSurfaceResponse'));b=s.index('\n#endif\n    // Keep the retired',a)
current=s[a:b]
classic='''    float source=WET_WEATHER_MODE==0?1.0:rainStrength;
    float moisture=clamp(source*smoothstep(0.18,0.88,sky)
        *(1.0-exp(-1.75*SURFACE_DAMPNESS))*(1.0+0.08*rainStrength),0.0,1.0);
    if(moisture>0.001&&WET_SHEEN>0.0){
        vec3 view=unitVector(-playerPoint);
        float nv=max(dot(n,view),0.0);
        if(nv>0.001){
            // Uniform material response retained; only exposure/angle vary.
            float roughness=mix(0.68,max(0.28,0.68*0.48),moisture);
            float film=moisture*mix(0.32,1.0,max(n.y,0.0))*WET_SHEEN;
            vec3 ray=reflect(-view,n),environment=softSkyReflection(ray);
            float exposure=sky*mix(0.12,1.0,smoothstep(-0.10,0.45,ray.y));
            float fresnel=classicWetFresnel(nv)*(1.0-0.42*roughness);
            float coat=clamp(film*fresnel,0.0,0.85);
            dry=mix(dry,environment*exposure,coat);
            float specular=classicWetSunSpecular(n,view,broadLightDirection(),roughness);
            float sun=solarDaylight()*sky*(1.0-0.75*rainStrength);
            dry+=sunlightColour()*0.72*specular*sun*film;
        }
    }'''
s=s[:a]+'#if WET_FILM_STYLE == 0\n'+classic+'\n#else\n'+current+'\n#endif'+s[b:];p.write_text(s)
# Bloom is an independent requested effect, including in vanilla light mode.
p=c/'output.frag.glsl';s=p.read_text().replace('    vec3 physicalColour = max(texture(colortex3, rasterUV).rgb, vec3(0.0));','''    vec3 physicalColour = max(texture(colortex3, rasterUV).rgb, vec3(0.0));
    if(BLOOM_STRENGTH>0.0)physicalColour+=max(texture(colortex6,rasterUV).rgb,vec3(0.0))*BLOOM_STRENGTH;''').replace('// bloom or highlight shoulder changes their brightness or ambient level.','// highlight shoulder changes their brightness or ambient level.\n    // Requested bloom remains independent of this lighting/colour bypass.').replace('    physicalColour += max(texture(colortex6, rasterUV).rgb, vec3(0.0)) * BLOOM_STRENGTH;\n','');p.write_text(s)
p=r/'shaders.properties';s=p.read_text().replace('# The vanilla transfer has no bloom contribution: avoid its two unused passes.\nprogram.composite5.enabled=false\nprogram.composite6.enabled=false\n','')
s=s.replace('screen.REFLECTIONS=REFLECTION_MODE','screen.REFLECTIONS=REFLECTION_TRACE REFLECTION_MODE').replace('screen.MATERIALS=WET_WEATHER_MODE','screen.MATERIALS=WET_FILM_STYLE WET_WEATHER_MODE')
s=re.sub(r'^(profile\.[^\n]+)$',r'\1 REFLECTION_TRACE:0 WET_FILM_STYLE:0',s,flags=re.M)
s=s.replace('#if REFLECTION_MODE != 0\n#if REFLECTION_MODE == 2\nsize.buffer.colortex16','#if REFLECTION_MODE != 0 && REFLECTION_TRACE == 1\n#if REFLECTION_MODE == 2\nsize.buffer.colortex16');p.write_text(s)
p=r/'lang/en_us.lang';s=p.read_text().replace('ground warmth, bloom and camera grading','ground warmth and camera grading').replace('Independent wet highlights, Stratus water and atmosphere remain.','Independent bloom, wet highlights, Stratus water and atmosphere remain.')
s+='''
option.REFLECTION_TRACE=Reflection renderer
option.REFLECTION_TRACE.comment=Classic restores1.3.1's16/28-depth-sample reflections and omits added reflected-mist integration. Detailed retains receiver-plane geometry tracing and reflected volumetric mist. Both retain the selected effect resolution, range and sky fallback; Classic can miss thin scenery. Temporal intersection hints apply to Detailed only.
value.REFLECTION_TRACE.0=Classic1.3.1 (default)
value.REFLECTION_TRACE.1=Detailed geometry
option.WET_FILM_STYLE=Wet sheen style
option.WET_FILM_STYLE.comment=Classic restores1.3.1 dielectric sky film and GGX sun highlights with common material roughness. Current retains the rc5 film. Both preserve weather/exposure, separate amount/sheen, zero controls and optional independent Original dampness; no forced pore darkening.
value.WET_FILM_STYLE.0=Classic1.3.1 (default)
value.WET_FILM_STYLE.1=Current restrained
''';p.write_text(s)
