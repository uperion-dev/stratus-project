from pathlib import Path
from zipfile import ZipFile
import re,json
w=Path(__file__).parent;dst=Path.home()/'Library/Application Support/ModrinthApp/profiles/Minecraft (1)/shaderpacks';rows=[]
def props(p):return dict(l.split('=',1) for l in p.read_text().splitlines() if '=' in l and not l.startswith('#'))
for base in sorted(w.glob('Stratus-1.7.0-rc6-QA-v*-*.zip')):
 with ZipFile(base) as z:s=z.read('shaders/core/options.glsl').decode()
 defaults=dict(re.findall(r'^#define (\w+) ([^\s]+)\s*//\s*\[',s,re.M));defaults.update(re.findall(r'^const float (\w+)\s*=\s*([^;]+);\s*//\s*\[',s,re.M))
 for f in [base,Path(str(base)+'.txt')]:
  target=dst/f.name
  if not target.exists():rows.append({'file':f.name,'result':'already absent (Iris may discard all-default options)'});continue
  same=target.read_bytes()==f.read_bytes() if f.suffix=='.zip' else defaults|props(target)==defaults|props(f)
  if same:target.unlink();action='removed owned exact/effective-equivalent QA file'
  else:action='preserved newer changed QA file'
  rows.append({'file':f.name,'result':action})
(w/'qa-cleanup.json').write_text(json.dumps(rows,indent=2)+'\n');print({tag:sum(r['result']==tag for r in rows) for tag in set(r['result'] for r in rows)})
