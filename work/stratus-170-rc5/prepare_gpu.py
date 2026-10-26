from pathlib import Path
import sys
sys.path.insert(0,str(Path('work/stratus-check').resolve()))
from prepare import expand,adapt,override
r=Path('outputs/Stratus/shaders').resolve();w=Path('work/stratus-170-rc5');n=w/'native';n.mkdir(exist_ok=True)
(n/'screen.vsh').write_text('#version 330 core\nvoid main(){vec2 p=vec2((gl_VertexID<<1)&2,gl_VertexID&2);gl_Position=vec4(p*2.0-1.0,0,1);}')
frame=expand(r/'core/frame.glsl',r);options=expand(r/'core/options.glsl',r)
trace=expand(r/'core/scene-trace.glsl',r).replace('ivec2 opticsSize','int receiverReads=0;\nivec2 opticsSize',1).replace('    ivec2 size=opticsSize(cache);cell=', '    receiverReads++;\n    ivec2 size=opticsSize(cache);cell=',1)
(n/'trace.fsh').write_text(adapt('#version 330 compatibility\n'+options+'\n'+frame+'\nuniform sampler2D depthtex1,colortex4;\n'+trace+'''\nuniform vec3 testOrigin,testDirection;uniform float testHint;uniform int testFresh;layout(location=0)out vec4 result;layout(location=1)out vec4 diagnostics;
void main(){float path;vec4 colour=traceOpticalSceneHint(testOrigin,unitVector(testDirection),vec3(0,1,0),1,2,80.0,path,testFresh==1?0.0:testHint);result=colour;diagnostics=vec4(path,float(receiverReads),0,1);}
''','frag'))
refraction=expand(r/'core/refraction.glsl',r).replace('// Restored','int depthReads=0;\nvec4 probeDepth(vec2 uv){depthReads++;return texture(depthtex1,uv);}\n// Restored',1).replace('texture(depthtex1,shifted)','probeDepth(shifted)').replace('texture(depthtex1,edge)','probeDepth(edge)')
(n/'refraction.fsh').write_text(adapt(override('#version 330 compatibility\n'+options+'\n'+frame+'\nuniform sampler2D depthtex1;\n'+refraction+'''\nuniform vec2 testUV;uniform float testHint;uniform vec3 testNormal;layout(location=0)out vec4 result;layout(location=1)out vec4 diagnostics;void main(){float rejected;vec2 uv=legacyWaterRefractionUV(testUV,testNormal,vec3(0,0,1),8.0,5.0,testHint,rejected);result=vec4(uv,0,1);diagnostics=vec4(rejected,float(depthReads),0,1);}
''',{'REFRACTION_QUALITY':'2'}),'frag'))
(n/'history.fsh').write_text(adapt('#version 330 compatibility\n'+override(options,{'TEMPORAL_OPTICS':'1'})+'\n'+expand(r/'core/temporal-optics.glsl',r)+'''\nuniform sampler2D history;layout(location=0)out vec4 result;void main(){result=vec4(previousOpticalHint(history,ivec2(0)),nextOpticalHint(7.0),1);}
''','frag'))

for quality in (0,1):
 (n/f'refraction-q{quality}.fsh').write_text(override((n/'refraction.fsh').read_text(),{'REFRACTION_QUALITY':str(quality)}))
