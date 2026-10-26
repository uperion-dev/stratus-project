#ifndef STRATUS_TEMPORAL_OPTICS_INCLUDED
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
