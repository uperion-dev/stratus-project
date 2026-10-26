from pathlib import Path
import json,re,zipfile
w=Path(__file__).parent;dst=Path.home()/'Library/Application Support/ModrinthApp/profiles/Minecraft (1)/shaderpacks';rows=[]
def props(p):return dict(l.split('=',1) for l in p.read_text().splitlines() if '=' in l and not l.startswith('#'))
for base in sorted(w.glob('Stratus-1.7.0-rc5-QA-v2-*.zip')):
 with zipfile.ZipFile(base) as z:s=z.read('shaders/core/options.glsl').decode()
 defaults=dict(re.findall(r'^#define (\w+) ([^\s]+)\s*//\s*\[',s,re.M));defaults.update(re.findall(r'^const float (\w+)\s*=\s*([^;]+);\s*//\s*\[',s,re.M))
 for f in [base,Path(str(base)+'.txt')]:
  target=dst/f.name
  if not target.exists():continue
  same=target.read_bytes()==f.read_bytes() if f.suffix=='.zip' else defaults|props(target)==defaults|props(f)
  if same:target.unlink();action='removed owned unchanged/effective-equivalent QA file'
  else:action='preserved newer changed QA file'
  rows.append({'file':f.name,'result':action})
(w/'qa-v2-cleanup.json').write_text(json.dumps(rows,indent=2)+'\n')
