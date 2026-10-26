from pathlib import Path
import shutil,re,json
w=Path(__file__).parent; src=Path('outputs/Stratus-1.7.0-rc5.zip')
# Final candidate bytes for both variants, only saved switch differs.
for label,value in [('On','1'),('Off','0')]:
 name=f'Stratus-1.7.0-rc5-QA-v2-{label}.zip';shutil.copy2(src,w/name)
 s=(w/'initial-rc3-settings.txt').read_text();s='\n'.join(l for l in s.splitlines() if not l.startswith('TEMPORAL_OPTICS='))+f'\nTEMPORAL_OPTICS={value}\n';(w/(name+'.txt')).write_text(s)
# Never overwrite the first phase's restoration snapshot/evidence.
for name in ['visual-original-client-state.txt','visual-driver-stopped.txt','visual-complete.txt']:
 f=w/name
 if f.exists():shutil.copy2(f,w/('phase1-'+name))
s=Path('work/stratus-170-rc4/agent/VisualRc4.java').read_text().replace('VisualRc4','VisualBenchRc5').replace('ChunkGateRc4','ChunkGateRc5').replace('stratus-170-rc4','stratus-170-rc5').replace('VISUAL_RC4','VISUAL_BENCH_RC5').replace('Stratus-1.7.0-rc4','Stratus-1.7.0-rc5')
s=s.replace('((Executor)client).execute(this::poll);','CompletableFuture<Void> queued=new CompletableFuture<>();\n                    ((Executor)client).execute(()->{try{poll();}finally{queued.complete(null);}});queued.join();')
s=s.replace('visual-original-client-state.txt','bench-original-client-state.txt').replace('visual-driver-stopped.txt','bench-driver-stopped.txt')
(w/'agent/VisualBenchRc5.java').write_text(s)
s=Path('work/stratus-refine-1611/agent/ActiveBenchmark1611.java').read_text().replace('ActiveBenchmark1611','ActiveBenchRc5').replace('stratus-refine-1611','stratus-170-rc5')
s=s.replace('Thread t=new Thread(()->{try{while(!Files.exists(w.resolve("activity-stop.txt")))','Thread t=new Thread(()->{long deadline=System.currentTimeMillis()+300000;try{while(System.currentTimeMillis()<deadline&&!Files.exists(w.resolve("activity-stop.txt")))')
s=s.replace('((Executor)client).execute(()->{try{','java.util.concurrent.CompletableFuture<Void> queued=new java.util.concurrent.CompletableFuture<>();((Executor)client).execute(()->{try{')
s=s.replace('catch(Exception ignored){}}});Thread.sleep(5000);','catch(Exception ignored){}}finally{queued.complete(null);}});queued.join();Thread.sleep(5000);')
(w/'agent/ActiveBenchRc5.java').write_text(s)
# Existing STOP packet was consumed; no stale commands permitted.
f=w/'visual-request.txt'
if f.exists():raise RuntimeError('Unconsumed previous command file')
