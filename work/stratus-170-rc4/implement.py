from pathlib import Path
p=Path('outputs/Stratus/shaders')
f=p/'core/options.glsl';s=f.read_text().replace('#define TEMPORAL_ATMOSPHERE 1 // [0 1]','#define TEMPORAL_ATMOSPHERE 1 // [0 1]\n#define ORIGINAL_DAMPNESS 0.00 // [0.00 0.10 0.20 0.30 0.40 0.50 0.65 0.80 1.00 1.25 1.50 2.00]');f.write_text(s)
f=p/'shaders.properties';s=f.read_text().replace('screen.MATERIALS=WET_WEATHER_MODE SURFACE_DAMPNESS WET_SHEEN WET_DARKENING','screen.MATERIALS=WET_WEATHER_MODE SURFACE_DAMPNESS WET_SHEEN ORIGINAL_DAMPNESS WET_DARKENING <empty>');s='\n'.join(l+' ORIGINAL_DAMPNESS:0.00' if l.startswith('profile.') else l for l in s.splitlines())+'\n';s=s.replace('sliders=','sliders=ORIGINAL_DAMPNESS ',1);f.write_text(s)
f=p/'lang/en_us.lang';s=f.read_text()+'\noption.ORIGINAL_DAMPNESS=Original dampness\noption.ORIGINAL_DAMPNESS.comment=Restores optional porous-material absorption darkening and the original humidity/shelter/drainage response. Zero is off and preserves the current diffuse palette. Independent of surface film and sheen controls; nonporous materials stay unchanged. This is a local approximation, not stored wetness over time. The retired WET_DARKENING setting stays a no-op.\n';f.write_text(s)
f=p/'core/diffuse.glsl';s=f.read_text().replace('// Material.x remains in the buffer for saved-layout compatibility, not gating.','// Material absorption is used only by the separate optional original dampness.\n// Film reflectance and roughness are deliberately uniform across materials.')
a=s.index('vec3 wetSurfaceResponse');s=s[:a]+'''// Original project1.6.7 absorption shape, restored independently of sheen.
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
'''+s[a:]
s=s.replace('#if DIMENSION_TYPE == 0\n    float filmSource=', '''#if DIMENSION_TYPE == 0
    if(ORIGINAL_DAMPNESS>0.0){
        float moisture=originalSurfaceMoisture(sky,n,material.x);
        float saturation=moisture*(0.45+0.55*clamp(biomeHumidity,0.0,1.0));
        dry/=1.0+1.40*saturation*clamp(material.x,0.0,1.0);
    }
    float filmSource=''').replace('float exponent=mix(80.0,16.0,clamp(material.y,0.0,1.0));','// Same lobe for every material; normals/exposure still matter.\n            float exponent=mix(80.0,16.0,0.68);');f.write_text(s)
f=p/'core/moisture.glsl';s=f.read_text().replace('// No absorption darkening, retained dampness or extra reflection pass.','// Optional original absorption is independent; no extra reflection pass.').replace('if(SURFACE_DAMPNESS<=0.0||WET_SHEEN<=0.0)return dry;','if((SURFACE_DAMPNESS<=0.0||WET_SHEEN<=0.0)&&ORIGINAL_DAMPNESS<=0.0)return dry;').replace('Entities, held items, plants and emitters stay dry.','Entities, held items, excluded/back faces and emitters stay dry.').replace('vec2 material=texture(colortex2,uv).xy;','vec2 material=vec2(0.0,0.68);\n    if(ORIGINAL_DAMPNESS>0.0)material.x=texture(colortex2,uv).x;');f.write_text(s)
