#include "/core/water-optics.glsl"
in vec2 rasterUV;
#if TEMPORAL_OPTICS == 1 && REFRACTION_QUALITY > 0
/* RENDERTARGETS: 12,18 */
layout(location=1)out vec2 refractionHint;
#else
/* RENDERTARGETS: 12 */
#endif
layout(location=0)out vec4 completedScene;
void main(){vec2 hint;completedScene=vec4(computeWaterOptics(rasterUV,hint),1.0);
#if TEMPORAL_OPTICS == 1 && REFRACTION_QUALITY > 0
refractionHint=hint;
#endif
}
