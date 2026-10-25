from pathlib import Path
import sys
sys.path.insert(0,str(Path('work/stratus-check').resolve()));from prepare import expand,adapt,override
w=Path(__file__).parent;p=Path('outputs/Stratus/shaders').resolve()
base='#version 330 compatibility\n#define DIMENSION_TYPE 0\n'+expand(p/'core/options.glsl',p)+expand(p/'core/frame.glsl',p)+expand(p/'core/ceiling.glsl',p)+expand(p/'core/diffuse.glsl',p)+'\nuniform int probeMaterial;uniform vec3 probeNormal,probePoint;uniform float probeSky;layout(location=0)out vec4 result;void main(){result=vec4(wetSurfaceResponse(vec3(.3,.2,.1),probeNormal,probePoint,probeSky,wetMaterialProperties(probeMaterial)),1);}\n'
for tag,vals in {'film-uniform':{},'damp-zero':{'ORIGINAL_DAMPNESS':'0.00','SURFACE_DAMPNESS':'0.00','WET_SHEEN':'0.00'},'damp-half':{'ORIGINAL_DAMPNESS':'0.50','SURFACE_DAMPNESS':'0.00','WET_SHEEN':'0.00'},'damp-full':{'ORIGINAL_DAMPNESS':'1.00','SURFACE_DAMPNESS':'0.00','WET_SHEEN':'0.00'}}.items():(w/(tag+'.fsh')).write_text(adapt(override(base,vals),'.fsh'))
