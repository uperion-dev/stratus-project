from pathlib import Path
import subprocess,json
w=Path(__file__).parent
results={}
for q,name in [(0,'refraction-q0'),(1,'refraction-q1'),(2,'refraction')]:
 p=subprocess.run([str(w/'optics_probe'),str(w/'native'),name],capture_output=True,text=True)
 (w/f'gpu-q{q}.stderr.txt').write_text(p.stderr)
 if p.returncode:raise RuntimeError(p.stdout+p.stderr)
 row=json.loads(p.stdout);assert row['failures']==0 and row['gl_error']==0;results[str(q)]=row
(w/'optics-checks-final.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
