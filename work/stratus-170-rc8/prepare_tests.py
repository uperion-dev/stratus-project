from pathlib import Path
import zipfile,sys
sys.path.insert(0,str(Path('work/stratus-check').resolve()))
from prepare import expand,adapt,override
w=Path('work/stratus-170-rc8');r=Path('outputs/Stratus/shaders').resolve();old=(w/'baseline/shaders').resolve()
(w/'screen.vsh').write_text('#version 330 core\nout vec2 rasterUV;void main(){vec2 p=vec2((gl_VertexID<<1)&2,gl_VertexID&2);rasterUV=p;gl_Position=vec4(p*2.-1.,0,1);}')
for name,root,file in [('before-lake',old,'lake.frag.glsl'),('before-resolve',old,'water-resolve.frag.glsl'),('after-resolve',r,'water-resolve.frag.glsl')]:
 s='#version 330 compatibility\n#define DIMENSION_TYPE 0\n'+expand(root/'core'/file,root)
 (w/(name+'.fsh')).write_text(adapt(override(s,{'WATER_RENDER_QUALITY':'2','REFLECTION_MODE':'0','TEMPORAL_OPTICS':'0','WATER_STYLE':'0'}),'.fsh'))
# Independent exact archived reference for the realistic component.
with zipfile.ZipFile('outputs/Stratus-1.3.1.zip') as z:s=z.read('shaders/core/diffuse.glsl').decode()
a=s.index('vec3 formIrradiance');e=s.index('\nfloat waterFresnel',a);ref=s[a:e].replace('formIrradiance','referenceFace')
shared=''.join(expand(r/'core'/f'{lib}.glsl',r)+'\n' for lib in ['options','frame','ceiling','diffuse','entity-lighting'])
s='#version 330 compatibility\n#define DIMENSION_TYPE 0\n'+shared+ref+'''\nuniform vec3 probeNormal;uniform float probeSky;uniform int probeMode;layout(location=0)out vec4 result;
void main(){vec3 n=normalize(probeNormal);if(probeMode==0)result=vec4(abs(formIrradiance(n,probeSky)-referenceFace(n,probeSky)),1);else result=vec4(vec3(nativeEntityLighting(n)),1);}\n'''
(w/'faces.fsh').write_text(adapt(override(s,{'FACE_BLEND':'1.00','FACE_SHADING':'1.00','VANILLA_FACE_CONTRAST':'1.00','REALISTIC_FACE_CONTRAST':'1.00'}),'.fsh'))
