from pathlib import Path
import json,hashlib,shutil,html
w=Path(__file__).resolve().parent;r=w.parents[1]/'outputs/Stratus-1.7.0-rc4-visual-checks';(r/'captures').mkdir(parents=True,exist_ok=True)
notes={
'rc4-before-panels.png':'rc3 baseline, original saved quality at854x480. Native textures differ; full loaded-chunk gate passed.',
'rc4-uniform-panels.png':'Uniform film response, original dampness0. Same native texture palette retained. Exact material-response equality is isolated by the GPU constant-colour cases.',
'rc4-dry-panels.png':'Both film/sheen and original dampness off. Native material comparison.',
'rc4-damp-half.png':'Original dampness0.5 with film unchanged. Porous panels moderately darken; nonporous iron/gold sample regions unchanged.',
'rc4-damp-full.png':'Original dampness1.0, matched scene. Porous panels darken further; same iron/gold sample regions unchanged.',
'rc4-close-before.png':'Closer rc3 baseline. Left to right: wool,leaves,wood,gold,iron,quartz,sandstone,dirt,stone. Same geometry/light for all panels.',
'rc4-close-uniform.png':'Closer uniform sheen, original dampnessoff. Same lobe/reflectance does not force different textures and native colours to look identical.',
'rc4-close-dry.png':'Closer dry reference, all film/sheen/original dampness zeros. No hidden dampness from the retired control.',
'rc4-close-damp-half.png':'Closer0.5 original dampness. Fixed local humidity/exposure; no stored wetness simulation.',
'rc4-close-damp-full.png':'Closer1.0 original dampness. Graded porous darkening visible with nonporous panels stable.',
'rc4-release-panels.png':'Exact installed final rc4 ZIP loaded, original dampnessdefault0 and every saved prior override preserved. Full loaded-chunk gate passed.'}
log=(Path.home()/'Library/Application Support/ModrinthApp/profiles/Minecraft (1)/logs/latest.log').read_text();(w/'runtime-qa.log').write_text('\n'.join(l for l in log.splitlines() if 'STRATUS_VISUAL_RC4' in l)+'\n')
rows=[]
for name,note in notes.items():
 f=w/'screenshots'/name;assert f.exists();shutil.copy2(f,r/'captures'/name);rows.append({'file':'captures/'+name,'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'review':note})
manifest={'version':'1.7.0-rc4','profile':'Main / Minecraft (1)','world':'Stratus Terrain Lab','framebuffer':[854,480],'render_distance':12,'time':1000,'rain':0,'matched_saved_quality':True,'FPS_samples':0,'status':'Material candidate installed and loaded; finite panel review. Focused performance explicitly skipped.','limits':['Native textures/colours/face geometry/exposure still affect apparent sheen; class-independent response tested separately on GPU.','Wet weather/shelter behaviour checked by controlled GPU inputs, not a new exhaustive live rain/world acceptance.','Return-world stable gate failed to settle, even though final snapshot showed all columns/queues ready. Capture was cancelled; no accepted final return-world image.','Prior waterline/leaf-cluster/temporal acceptance remains in earlier batches.'],'captures':rows}
(r/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');(w/'review-notes.json').write_text(json.dumps(notes,indent=2)+'\n')
parts=['<!doctype html><html lang="en-AU"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Stratus1.7.0-rc4 checks</title><style>body{background:#121b29;color:#edf4fb;font:16px/1.5 system-ui;margin:0}main{max-width:1200px;margin:auto;padding:24px}a{color:#a7dcff}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,440px),1fr));gap:20px}figure{margin:0;background:#233247;border-radius:8px;overflow:hidden}img{width:100%;display:block}figcaption{padding:14px}.note{padding:16px;background:#49392d}</style><main><h1>Stratus1.7.0-rc4</h1><p>Uniform material film and optional original dampness.</p><p class="note">Actual matched854×480 Minecraft panel views. Resolution and saved quality preserved. Native textures differ; GPU tests isolate equal sheen response. Focused FPS skipped by user; no performance improvement claimed. Return-world readiness did not settle and that capture was cancelled. Earlier unresolved waterline/leaf/temporal work remains separate.</p><p><a href="../Stratus-1.7.0-rc4.zip">Candidate ZIP</a> · <a href="../Stratus-1.7.0-rc4-install.json">Install/load receipt</a> · <a href="manifest.json">Evidence and limits</a></p><div class="grid">']
for row in rows:parts.append('<figure><img loading="lazy" src="'+html.escape(row['file'])+'" alt="'+html.escape(Path(row['file']).stem)+'"><figcaption><strong>'+html.escape(Path(row['file']).stem)+'</strong><p>'+html.escape(row['review'])+'</p></figcaption></figure>')
parts.append('</div></main></html>');(r/'index.html').write_text(''.join(parts));print(len(rows),'reviewed captures')
