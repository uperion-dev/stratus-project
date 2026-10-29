from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
import shutil,json
w=Path(__file__).parent;r=Path('outputs/Stratus');settings=(w/'initial-rc5-settings.txt').read_text();records=[]
variants={'Before':{},'Restored':{},'Dry':{'SURFACE_DAMPNESS':'0.00','WET_SHEEN':'0.00','ORIGINAL_DAMPNESS':'0.00','BLOOM_STRENGTH':'0.00'},'BloomZero':{'BLOOM_STRENGTH':'0.00'},'BloomSmall':{'BLOOM_STRENGTH':'0.35','BLOOM_RADIUS':'0.50'},'BloomWide':{'BLOOM_STRENGTH':'0.35','BLOOM_RADIUS':'4.00'},'Original131':{}}
for label,overrides in variants.items():
 name=f'Stratus-1.7.0-rc6-QA-v1-{label}.zip';f=w/name
 if label in ['Before','Original131']:shutil.copy2(Path('outputs')/('Stratus-1.7.0-rc5.zip' if label=='Before' else 'Stratus-1.3.1.zip'),f)
 else:
  with ZipFile(f,'w',ZIP_DEFLATED) as z:
   for p in sorted((r/'shaders').rglob('*')):
    if p.is_file() and p.name!='.DS_Store':z.write(p,p.relative_to(r))
 s=(w/'initial-131-settings.txt').read_text() if label=='Original131' else settings
 vals=dict(l.split('=',1) for l in s.splitlines() if '=' in l and not l.startswith('#'));vals.update(overrides)
 (w/(name+'.txt')).write_text('# QA only; initial settings preserved separately\n'+''.join(f'{k}={v}\n' for k,v in sorted(vals.items())))
 records.append({'name':name,'scope':'exact131 with its saved settings; not equal quality to newer sky' if label=='Original131' else 'captured rc5 manual settings plus named overrides','overrides':overrides})
(w/'qa-packages.json').write_text(json.dumps(records,indent=2)+'\n')
s=Path('work/stratus-170-rc5/agent/VisualFinalBenchRc5.java').read_text().replace('VisualFinalBenchRc5','VisualRc6').replace('ChunkGateRc5','ChunkGateRc6').replace('stratus-170-rc5','stratus-170-rc6').replace('Stratus-1.7.0-rc5','Stratus-1.7.0-rc6').replace('Stratus-1.7.0-rc3.zip','Stratus-1.7.0-rc5.zip').replace('VISUAL_BENCH_RC5','VISUAL_RC6').replace('refbench-original-client-state','visual-original-client-state').replace('refbench-driver-stopped','visual-driver-stopped')
(w/'agent/VisualRc6.java').write_text(s)
s=Path('work/stratus-170-rc5/agent/ChunkGateRc5.java').read_text().replace('ChunkGateRc5','ChunkGateRc6');(w/'agent/ChunkGateRc6.java').write_text(s)
s=Path('work/stratus-170-rc4/agent/PanelsRc4.java').read_text().replace('PanelsRc4','PanelsRc6').replace('stratus-170-rc4','stratus-170-rc6');s=s.replace('for(String cmd:commands)', '''for(int j=0;j<types.length;j++)commands.add("fill "+(4200+j*2)+" 160 4205 "+(4201+j*2)+" 160 4211 minecraft:"+types[j]);commands.add("setblock 4208 166 4204 minecraft:sea_lantern");for(String cmd:commands)''');(w/'agent/PanelsRc6.java').write_text(s)
