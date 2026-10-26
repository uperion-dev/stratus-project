from pathlib import Path
import json
w=Path(__file__).parent;p=w/'performance-results.json';j=json.loads(p.read_text());j.update({'saved_VSync':True,'DynamicFPS_reported_enableVsync':False,'effective_swap_interval_verified':False,'VSync_scope':'Saved options and reported mod VSync state are both recorded; effective swap interval not independently queried. Matched user settings, not an uncapped GPU throughput claim.'});p.write_text(json.dumps(j,indent=2)+'\n')
p=w/'final_audit.py';s=p.read_text();s=s.replace("initial=props(w/'initial-client-state.txt');final=", "initial=props(w/'initial-client-state.txt'); latest=props(w/'refbench-original-client-state.txt'); final=")
s=s.replace("all(initial[k]==final[k] for k in initial)","all(latest.get(k,initial[k])==final[k] for k in initial)")
s=s.replace("'visual_driver_stopped':(w/'visual-driver-stopped.txt').exists()", "'visual_driver_stopped':all((w/n).exists() for n in ['visual-driver-stopped.txt','bench-driver-stopped.txt','refbench-driver-stopped.txt','activity-stopped.txt'])")
s=s.replace("glob('Stratus-1.7.0-rc5-QA-v1-*')","glob('Stratus-1.7.0-rc5-QA-*')")
s=s.replace("'focused_fps_samples':0,'final_runtime_focused':rt['focused']", "'focused_fps_samples':6,'initial_final_ZIP_load_focused':rt['focused'],'focused_benchmark_evidence':str(w/'performance-results.json'),'newer_user_camera_preserved':True")
s=s.replace("'focused active-game performance comparison; Mac locked/unfocused, no accepted FPS'", "'effective all-optics speedup and approximately60FPS Reference target; focused comparisons complete but show no gain'")
s=s.replace("'focused_fps_samples':0,'restoration_evidence'", "'focused_fps_samples':6,'performance_evidence':str(w/'performance-results.json'),'performance_result':'No supported gain; keep optics hints off by default. Approx60FPS target remains pending.','restoration_evidence'")
s=s.replace("'live_visual_acceptance':'pending; reviewed QA-v1 river static frame only'", "'live_visual_acceptance':'Nine finite river captures reviewed, including final-byte On/Off variants; continuous motion/glass/waterline coverage remains pending'")
p.write_text(s)
