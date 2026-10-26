from pathlib import Path
import zipfile,json,hashlib
w=Path(__file__).parent; source=Path('outputs/Stratus'); records=[]
settings=(w/'initial-rc3-settings.txt').read_text()
for label,value in [('On','1'),('Off','0')]:
 name=f'Stratus-1.7.0-rc5-QA-v1-{label}.zip';p=w/name
 with zipfile.ZipFile(p,'w',zipfile.ZIP_DEFLATED) as z:
  for f in sorted((source/'shaders').rglob('*')):
   if f.is_file() and f.name!='.DS_Store':z.write(f,f.relative_to(source))
 s='\n'.join(l for l in settings.splitlines() if not l.startswith('TEMPORAL_OPTICS='))+f'\nTEMPORAL_OPTICS={value}\n';(w/(name+'.txt')).write_text(s)
 records.append({'name':name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'temporal_optics':value})
(w/'qa-packages.json').write_text(json.dumps(records,indent=2)+'\n')
# Guarded driver reuses the established normal-world readiness/capture gates.
s=Path('work/stratus-170-rc4/agent/VisualRc4.java').read_text().replace('VisualRc4','VisualRc5').replace('ChunkGateRc4','ChunkGateRc5').replace('stratus-170-rc4','stratus-170-rc5').replace('VISUAL_RC4','VISUAL_RC5').replace('Stratus-1.7.0-rc4','Stratus-1.7.0-rc5')
(w/'agent/VisualRc5.java').write_text(s)
s=Path('work/stratus-170-rc4/agent/ChunkGateRc4.java').read_text().replace('ChunkGateRc4','ChunkGateRc5');(w/'agent/ChunkGateRc5.java').write_text(s)
