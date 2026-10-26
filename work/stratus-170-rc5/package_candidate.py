from pathlib import Path
import json,hashlib
w=Path(__file__).parent;p=Path('outputs/Stratus')
checks={'version':'1.7.0-rc5','batch':'c3ec7834-5d1e-403e-9eb7-7a12a3226909','status':'experimental default-off candidate; acceptance pending','native_pairs':768,'native_failures':0,'compile_log':str(w/'compile-final.log'),'optics_gpu':json.loads((w/'optics-checks-final.json').read_text()),'controls':json.loads((w/'control-checks.json').read_text()),'migration':json.loads((w/'migration-checks.json').read_text()),'live_scope':'QA-v1 On loaded, one reviewed 1440x842 river frame; 5124ms stable chunk gate. Unfocused/1FPS, not effective temporal reuse acceptance. Mac locked. Final candidate loading tracked externally.','focused_fps_samples':0,'pending':['matched On/Off motion/disocclusion/glass/waterline/reload/resize acceptance','full requested optics coverage beyond conservative search hints','focused active gameplay FPS and approximately60FPS target'],'default_TEMPORAL_OPTICS':0}
(p/'CHECKS.json').write_text(json.dumps(checks,indent=2)+'\n')
source={str(f.relative_to(p)):hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted((p/'shaders').rglob('*')) if f.is_file() and f.name!='.DS_Store'}
(w/'final-shader-fingerprints.json').write_text(json.dumps(source,indent=2)+'\n')
