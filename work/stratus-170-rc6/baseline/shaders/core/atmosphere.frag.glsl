#include "/core/options.glsl"
#include "/core/frame.glsl"
#include "/core/ceiling.glsl"
#include "/core/volume.glsl"
#include "/core/scene-depth.glsl"
#include "/core/temporal-atmosphere.glsl"
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
in vec2 rasterUV;
/* RENDERTARGETS: 11 */
layout(location=0)out vec4 integratedAtmosphere;
void main(){
    if(isEyeInWater!=0){integratedAtmosphere=vec4(0.0);return;}
    #if TEMPORAL_ATMOSPHERE == 1
    ivec2 cell=ivec2(gl_FragCoord.xy);
    float tick=mod(float(worldTime),24000.0);
    if(cell==ivec2(0,0)){integratedAtmosphere=vec4(float(frameCounter%1024),floor(tick/64.0),mod(tick,64.0),rainStrength);return;}
    if(cell==ivec2(1,0)){integratedAtmosphere=vec4(viewWidth,viewHeight,blindness,darknessFactor);return;}
#endif
    float limit=sceneDistance(rasterUV),sky=sceneSkyExposure(rasterUV);
    vec3 ray=unitVector(mat3(gbufferModelViewInverse)*positionFromDepth(rasterUV,0.5));
    #if TEMPORAL_ATMOSPHERE == 1
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
    vec4 volume=completeAtmosphereSegment(cameraPosition,ray,limit,sky,true);
    integratedAtmosphere=vec4(volume.rgb*volume.a,volume.a);
#if TEMPORAL_ATMOSPHERE == 1
    if(limit>=6999.0)integratedAtmosphere.a=-1.0-volume.a;
#endif
}
