#ifndef STRATUS_MOISTURE_INCLUDED
#define STRATUS_MOISTURE_INCLUDED
// Thin film on exposed solid blocks, including non-porous materials.
// Optional original absorption is independent; no extra reflection pass.
vec3 materialMoisture(vec3 dry,vec3 viewPoint,vec2 uv){
#if DIMENSION_TYPE == 0
    if((SURFACE_DAMPNESS<=0.0||WET_SHEEN<=0.0)&&ORIGINAL_DAMPNESS<=0.0)return dry;
    vec4 surface=texture(colortex1,uv);
    if(surface.a<0.5)return dry; // Entities, held items, excluded/back faces and emitters stay dry.
    vec3 n=unitVector(surface.xyz),p=playerFromView(viewPoint);
    vec2 material=vec2(0.0,0.68);
    if(ORIGINAL_DAMPNESS>0.0)material.x=texture(colortex2,uv).x;
    float sky=texture(colortex0,uv).r;
    return wetSurfaceResponse(dry,n,p,sky,material);
#else
    return dry;
#endif
}
#endif
