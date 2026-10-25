from pathlib import Path
import json,zipfile,tempfile,importlib.util
w=Path(__file__).parent;p=Path('outputs/Stratus');spec=importlib.util.spec_from_file_location('installer',p/'install.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);policy=json.loads((p/'RELEASE-POLICY.json').read_text());checks=[]
def check(n,b):assert b,n;checks.append(n)
with tempfile.TemporaryDirectory() as tmp:
 root=Path(tmp);profile=root/'Main';packs=profile/'shaderpacks';packs.mkdir(parents=True);prev=packs/'Stratus-1.7.0-rc3.zip.txt';prev.write_text('# Prior values\nWATER_TEXTURE=0.50\nRIPPLE_SIZE=4.00\nREFLECTION_MODE=2\nWET_SHEEN=0.50\n');old=prev.read_bytes();archive=root/('Stratus-'+policy['version']+'.zip')
 with zipfile.ZipFile(archive,'w') as z:z.writestr('RELEASE-POLICY.json',json.dumps(policy))
 m.install(archive,profile,prev,True);check('Dry run writes nothing',not (packs/archive.name).exists());m.install(archive,profile,prev);settings=packs/(archive.name+'.txt');check('Every original override carried',m.read_values(settings)==m.read_values(prev));check('Old preferences byte-identical',prev.read_bytes()==old)
 for key,val in [('ORIGINAL_DAMPNESS','0.00'),('ORIGINAL_DAMPNESS','1.00'),('WET_DARKENING','1.30'),('TEMPORAL_ATMOSPHERE','0'),('TEMPORAL_ATMOSPHERE','1'),('WATER_STYLE','0'),('TRANSPARENT_REFLECTIONS','0.00'),('WATER_TEXTURE','0.00')]:
  carried,reset=m.migrate({key:val},policy);check('Manual '+key+'='+val+' preserved',carried[key]==val and not reset)
 check('Missing new option uses source default',m.migrate({},policy)==({},{}));settings.write_bytes(b'# Newer preferences\nTEMPORAL_ATMOSPHERE=0\n');newer=settings.read_bytes();again=m.install(archive,profile,prev);check('Existing new release preferences win',settings.read_bytes()==newer and again['existing_new_version_preferences_preserved']);check('Atomic create never overwrites',not m.create_if_absent(settings,b'wrong'))
 archive.write_bytes(archive.read_bytes()+b'changed')
 try:m.install(archive,profile,prev)
 except FileExistsError:checks.append('Conflicting archive refused')
 else:raise AssertionError('Archive conflict lost')
report={'checks':checks,'failures':0,'scope':'Actual candidate policy and installer in temporary profiles'};(w/'migration-checks.json').write_text(json.dumps(report,indent=2)+'\n');print(len(checks),'checks pass')
