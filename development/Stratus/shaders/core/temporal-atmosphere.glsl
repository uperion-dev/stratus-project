#ifndef STRATUS_TEMPORAL_ATMOSPHERE
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
