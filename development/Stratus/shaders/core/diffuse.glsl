#ifndef STRATUS_DIFFUSE_INCLUDED
#define STRATUS_DIFFUSE_INCLUDED
// Approximate properties for ordinary textures without PBR maps.
// x: water-absorption response, y: perceptual roughness. These are independent:
// rough metal/glazed ceramic still has zero pore absorption. Heuristic classes,
// not measured porosity. Stone and embedded ores share a class.
vec2 wetMaterialProperties(int material) {
    if (material == 4110) return vec2(0.90, 0.96);
    if (material == 4111) return vec2(0.64, 0.80);
    if (material == 4113) return vec2(0.02, 0.68);
    if (material == 4114 || (material>=4120&&material<=4123)) return vec2(0.00, 0.38);
    if (material == 4115) return vec2(0.80, 0.98);
    if (material == 4116) return vec2(0.16, 0.48);
    if (material == 4117) return vec2(0.72, 0.91);
    return vec2(0.45, 0.86);
}
vec3 formIrradiance(vec3 normal, float skyExposure) {
    float vertical=normal.y>=0.0?1.0:0.5;
    float vanilla=dot(normal*normal,vec3(0.6,vertical,0.8));
    float upperHemisphere = 0.5 + 0.5 * normal.y;
    vec3 sky = mix(vec3(0.31, 0.295, 0.275), vec3(1.025, 1.0, 0.95), upperHemisphere);
    vec3 skyKey=unitVector(broadLightDirection()+vec3(-0.20,0.0,0.13));
    float directional = max(dot(normal, skyKey), 0.0);
    sky += sunlightColour() * 0.23 * directional * daytimeWeight() * (1.0 - 0.65 * rainStrength);
    sky /= 1.12;
    // The lightmap has no point-light positions: retain broad indoor fill.
    float indoor = 0.72 + 0.20 * max(normal.y, 0.0) - 0.12 * max(-normal.y, 0.0);
    vec3 physical = mix(vec3(indoor), sky, smoothstep(0.04, 0.85, skyExposure));
    // Separate controls: realistic=1/vanilla=1 reproduces the original
    // 1.3.1 form response; zero remains an exact component bypass.
    vec3 realistic=mix(vec3(1.0),physical,REALISTIC_FACE_CONTRAST);
    vec3 irradiance=realistic*mix(1.0,vanilla,FACE_BLEND*VANILLA_FACE_CONTRAST);
    return mix(vec3(1.0),irradiance,FACE_SHADING);
}
// A surface film adds reflected highlights without changing the diffuse albedo.
// Absorption darkening/retained dampness was deliberately retired in 1.6.9.
// Material absorption is used only by the separate optional original dampness.
// Film reflectance and roughness are deliberately uniform across materials.
// Original project1.6.7 absorption shape, restored independently of sheen.
// The new amount replaces the old coupled dampness/darkening controls.
float originalSurfaceMoisture(float sky,vec3 n,float absorption){
#if DIMENSION_TYPE == 0
    float humidity=clamp(biomeHumidity,0.0,1.0);
    float upward=smoothstep(-0.15,0.85,n.y);
    float exposed=smoothstep(0.12,0.83,sky)*(0.40+0.30*humidity+0.25*rainStrength)
        *mix(0.55,1.0,upward);
    float shelter=smoothstep(0.02,0.22,sky)*(1.0-smoothstep(0.22,0.85,sky));
    float retained=humidity*clamp(absorption,0.0,1.0)*shelter*(0.10+0.12*upward);
    return clamp(ORIGINAL_DAMPNESS*(exposed+retained),0.0,1.0);
#else
    return 0.0;
#endif
}
float classicWetFresnel(float cosine) {
    return 0.0204 + 0.9796 * pow(1.0 - clamp(cosine, 0.0, 1.0), 5.0);
}
float classicWetSunSpecular(vec3 n, vec3 v, vec3 l, float roughness) {
    float nv = max(dot(n, v), 0.001), nl = max(dot(n, l), 0.0);
    if (nl <= 0.0) return 0.0;
    vec3 h = unitVector(v + l);
    float nh = max(dot(n, h), 0.0), vh = max(dot(v, h), 0.0);
    float alpha = max(roughness * roughness, 0.08), a2 = alpha * alpha;
    float denominator = nh * nh * (a2 - 1.0) + 1.0;
    float distribution = a2 / max(3.14159265 * denominator * denominator, 0.00001);
    float visibility = 0.5 / max(nl * sqrt(nv * nv * (1.0 - a2) + a2)
                        + nv * sqrt(nl * nl * (1.0 - a2) + a2), 0.0001);
    return distribution * visibility * classicWetFresnel(vh) * nl;
}

vec3 wetSurfaceResponse(vec3 dry,vec3 n,vec3 playerPoint,float sky,vec2 material){
#if DIMENSION_TYPE == 0
    if(ORIGINAL_DAMPNESS>0.0){
        float moisture=originalSurfaceMoisture(sky,n,material.x);
        float saturation=moisture*(0.45+0.55*clamp(biomeHumidity,0.0,1.0));
        dry/=1.0+1.40*saturation*clamp(material.x,0.0,1.0);
    }
#if WET_FILM_STYLE == 0
    float source=WET_WEATHER_MODE==0?1.0:rainStrength;
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
    }
#else
    float filmSource=WET_WEATHER_MODE==0?1.0:rainStrength;
    float film=filmSource*SURFACE_DAMPNESS*smoothstep(0.18,0.85,sky)
        *mix(0.78,1.0,clamp(n.y*0.5+0.5,0.0,1.0));
    if(WET_SHEEN>0.0&&film>0.0001){
        vec3 view=unitVector(-playerPoint);
        float nv=max(dot(n,view),0.0);
        if(nv>0.001){
            float fresnel=0.08+0.92*pow(1.0-nv,5.0);
            float coat=clamp(film*WET_SHEEN*fresnel*0.25,0.0,0.22);
            vec3 environment=softSkyReflection(reflect(-view,n));
            // Reflection can be lighter or darker than a white block. This is
            // angle-dependent film, never absorption or diffuse recolouring.
            dry=mix(dry,environment,coat);
            vec3 light=broadLightDirection(),halfway=unitVector(view+light);
            // Same lobe for every material; normals/exposure still matter.
            float exponent=mix(80.0,16.0,0.68);
            float lobe=pow(max(dot(n,halfway),0.0),exponent)*(exponent+2.0)/6.283185307;
            dry+=sunlightColour()*solarDaylight()*max(dot(n,light),0.0)
                *lobe*film*WET_SHEEN*0.008*(1.0-0.65*rainStrength);
        }
    }
#endif
#endif
    // Keep the retired option discoverable by Iris; every allowed value is a no-op.
    return dry+vec3(0.0)*WET_DARKENING;
}
vec3 diffuseRadiance(vec3 colour, vec3 mappedLight, float skyExposure, vec3 worldNormal,
                     float kind, vec3 playerPoint, int material) {
    if (kind < 0.5) return decodeDisplay(colour);
#if REALISTIC_LIGHTING == 0
    // oldLighting=true supplies Minecraft's original vertex face shading/AO.
    // Vanilla multiplies texture/vertex colour by the game's lightmap in display
    // space. Decode their product once, then bypass artistic grading at output.
    return decodeDisplay(colour*mappedLight);
#else
    vec3 normal = unitVector(worldNormal);
    if (dot(normal, normal) < 0.1) normal = vec3(0.0, 1.0, 0.0);
    float lampShare = 1.0 - smoothstep(0.08, 0.85, skyExposure) * daytimeWeight();
    vec3 light = decodeDisplay(mappedLight) * mix(LAMP_LEVEL, SKY_AMBIENT, skyExposure);
    light *= mix(vec3(1.0), vec3(1.015, 0.985, 0.87), LAMP_HEAT * lampShare);
    // Entities, held items and blocks get form lighting; billboard quads do not.
    vec3 form = kind > 0.95 ? formIrradiance(normal, skyExposure) : vec3(1.0);
    // Material wetness is applied once by the opaque resolve (or late block pass).
    vec3 albedo = decodeDisplay(colour);
    vec3 reflected = albedo * light * form;
    if (kind > 1.5 && kind < 2.5) {
        float interior = smoothstep(0.48, 0.94, max(colour.r, max(colour.g, colour.b)));
        reflected = max(reflected, decodeDisplay(colour) * interior * LAMP_LEVEL * 2.1);
    }
    return reflected;
#endif
}
#endif
