from pathlib import Path
import json,zipfile,tempfile,importlib.util
w=Path(__file__).parent;p=Path('outputs/Stratus');sp=importlib.util.spec_from_file_location('installer',p/'install.py');m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);policy=json.loads((p/'RELEASE-POLICY.json').read_text());policy['version']='1.7.0-rc6';policy['reset_related_overrides']=[];checks=[]
def check(label,ok):assert ok,label;checks.append(label)
with tempfile.TemporaryDirectory() as t:
 root=Path(t);profile=root/'Main';packs=profile/'shaderpacks';packs.mkdir(parents=True);prev=packs/'Stratus-1.7.0-rc5.zip.txt';prev.write_text((w/'initial-rc5-settings.txt').read_text());before=prev.read_bytes();archive=root/'Stratus-1.7.0-rc6.zip'
 with zipfile.ZipFile(archive,'w') as z:z.writestr('RELEASE-POLICY.json',json.dumps(policy))
 m.install(archive,profile,prev,True);check('Dry run writes nothing',not (packs/archive.name).exists());m.install(archive,profile,prev);settings=packs/(archive.name+'.txt');check('All captured latest manual overrides carry',m.read_values(settings)==m.read_values(prev));check('Prior file byte-identical',prev.read_bytes()==before)
 for key in ['BLOOM_RADIUS','BLOOM_STRENGTH','WET_SHEEN','SURFACE_DAMPNESS','ORIGINAL_DAMPNESS','WET_DARKENING','REFLECTION_MODE','WATER_RENDER_QUALITY','ATMOSPHERE_QUALITY','TEMPORAL_OPTICS','TEMPORAL_ATMOSPHERE','REFLECTION_TRACE','WET_FILM_STYLE']:
  for value in ['0','1']:
   carried,reset=m.migrate({key:value},policy);check(f'Saved {key}={value} preserved',carried.get(key)==value and not reset)
 check('No related override reset',not policy['reset_related_overrides']);settings.write_text('# Newer user preference\nREFLECTION_TRACE=1\nWET_FILM_STYLE=1\nBLOOM_RADIUS=4.00\n');new=settings.read_bytes();m.install(archive,profile,prev);check('Existing new-version preferences win',settings.read_bytes()==new);check('Atomic write cannot overwrite',not m.create_if_absent(settings,b'bad'))
 archive.write_bytes(archive.read_bytes()+b'x')
 try:m.install(archive,profile,prev)
 except FileExistsError:checks.append('Conflicting archive refused')
 else:raise AssertionError('Conflict overwritten')
(w/'migration-checks.json').write_text(json.dumps({'checks':checks,'failures':0,'scope':'Actual installer and intended rc6 no-reset policy, temporary profiles'},indent=2)+'\n');print(len(checks),'migration checks pass')
