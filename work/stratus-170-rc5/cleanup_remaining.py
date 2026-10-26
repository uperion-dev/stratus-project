from pathlib import Path
import json,re,zipfile
w=Path(__file__).parent;dst=Path.home()/'Library/Application Support/ModrinthApp/profiles/Minecraft (1)/shaderpacks';target=dst/'Stratus-1.7.0-rc5-QA-v1-On.zip.txt';base=w/'Stratus-1.7.0-rc5-QA-v1-On.zip'
def props(p):return dict(l.split('=',1) for l in p.read_text().splitlines() if '=' in l and not l.startswith('#'))
with zipfile.ZipFile(base) as z:s=z.read('shaders/core/options.glsl').decode()
defaults=dict(re.findall(r'^#define (\w+) ([^\s]+)\s*//\s*\[',s,re.M));old=defaults|props(w/(base.name+'.txt'));new=defaults|props(target)
if old!=new:raise RuntimeError('New effective QA preference; preserving '+str(target))
rows=json.loads((w/'qa-cleanup.json').read_text());rows.append({'file':target.name,'result':'removed after QA-v1 archive-default plus effective-settings equality; Iris removed redundant TEMPORAL_OPTICS=1 and changed timestamp only'});target.unlink();(w/'qa-cleanup.json').write_text(json.dumps(rows,indent=2)+'\n')
