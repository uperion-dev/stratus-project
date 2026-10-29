from pathlib import Path
import sys
sys.path.insert(0,str(Path('work/stratus-check').resolve()));from prepare import expand,adapt,override
w=Path(__file__).parent;r=Path('outputs/Stratus/shaders').resolve();n=w/'native';n.mkdir(exist_ok=True)
(n/'screen.vsh').write_text('#version 330 core\nout vec2 rasterUV;void main(){vec2 p=vec2((gl_VertexID<<1)&2,gl_VertexID&2);rasterUV=p;gl_Position=vec4(p*2.0-1.0,0,1);}')
for name,shader in [('bloom-small','bloom-horizontal.frag.glsl'),('bloom-wide','bloom-horizontal.frag.glsl'),('output-bloom','output.frag.glsl'),('output-zero','output.frag.glsl')]:
 vals={'BLOOM_RADIUS':'0.50' if name=='bloom-small' else '4.00','REALISTIC_LIGHTING':'0','BLOOM_STRENGTH':'0.00' if name=='output-zero' else '0.18'}
 (n/(name+'.fsh')).write_text(adapt(override('#version 330 compatibility\n'+expand(r/'core'/shader,r),vals),'.fsh'))
# Actual fresh scene trace classic implementation and the exact1.3.1 original.
options=expand(r/'core/options.glsl',r);frame=expand(r/'core/frame.glsl',r)
old=Path('work/stratus-170-rc6/reference-131/shaders/core/trace.glsl').read_text();old=old.replace('#ifndef STRATUS_TRACE_INCLUDED','#ifndef STRATUS_OLD_TRACE').replace('#define STRATUS_TRACE_INCLUDED','#define STRATUS_OLD_TRACE')
for quality in [1,2]:
 common=override(options,{'REFLECTION_MODE':str(quality),'REFLECT_RANGE':'88.0'})
 before=old.replace('uniform sampler2D depthtex1;','').replace('uniform sampler2D colortex4;','')
 after=expand(r/'core/classic-reflection.glsl',r)
 for label,src,expr in [('before',before,'sceneryReflection(origin,unitVector(direction))'),('after',after,f'classicSceneryReflection(origin,unitVector(direction),vec3(0,1,0),1,{quality},88.0,path)')]:
  text='#version 330 compatibility\n'+common+frame+'\nuniform sampler2D depthtex1,colortex4;\n'+src+'\nuniform vec3 origin,direction;layout(location=0)out vec4 result;void main(){float path;result='+expr+';}\n'
  (n/f'trace-{quality}-{label}.fsh').write_text(adapt(text,'.fsh'))
