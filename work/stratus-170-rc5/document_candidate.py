from pathlib import Path
import json,sys
sys.path.insert(0,str(Path('work/stratus-check').resolve()));from prepare import profiles
w=Path(__file__).parent;p=Path('outputs/Stratus');version='1.7.0-rc5'
policy=json.loads((p/'RELEASE-POLICY.json').read_text());policy['version']=version;policy['reset_related_overrides']=[];policy['visual_defaults']=profiles((p/'shaders').resolve())['REFERENCE'];policy['notes']='Experimental optical intersection/shoreline hints, default off in all presets. Preserve every existing override. No measured gameplay speedup or full temporal-optics acceptance.'
(p/'RELEASE-POLICY.json').write_text(json.dumps(policy,indent=2)+'\n')
f=p/'package.py';f.write_text(f.read_text().replace("'Stratus-1.7.0-rc4.zip'","'Stratus-1.7.0-rc5.zip'"))
(p/'README.txt').write_text('''STRATUS 1.7.0-rc5 — EXPERIMENTAL TEMPORAL OPTICS HINTS
Original Iris shader pack, MIT licensed. Candidate; not full 1.7 acceptance.

New optional Temporal optics hints switch in Reflections/Performance, default
Off in all four presets. This extends temporal work beyond sky atmosphere:
- Water and thin transparent-solid scenery reflection searches try the preceding
  frame's intersection distance as a current-plane search seed. Current depth,
  normals, medium-side tests, foreground traversal and current colour remain.
- Water refraction tries the previously rejected shoreline guard first, using
  current depth. Every accepted ray still runs the full selected guard set.

These are geometry/search hints, not colour accumulation or renderer frame
skipping. Waves, animated textures and reflected colours evaluate freshly.
Cheap sky/environment lookup, single-guard thin-glass refraction and the
unbent underwater exit remain fresh. This candidate does not claim temporal
radiance reuse across all optics or a measured gameplay FPS improvement.

All 67 previous controls/defaults/choices/preset assignments remain, including
optional Original dampness and retired WET_DARKENING. New switch gives 68
controls. No existing override resets; existing new-release preferences win.
Quality, resolution, ray budgets and draw distance are preserved. On uses up
to three extra RG16F history pairs in existing passes (no new pass); storage
and invalid hints can cost performance. Off removes those history outputs.
At 1440x842 with full scenery reflections and half water, raw paired history
storage is about 21.8 MB (20.8 MiB), excluding driver alignment/overhead.
Sky-only/quality-zero branches omit their unused hint attachments.

Install: use install.py with this release ZIP to preserve latest saved settings.
Earlier release archives/settings remain intact. Technical checks and finite
QA are described in VALIDATION.txt/CHECKS.json. Actual final-release loading,
visual and performance acceptance are recorded separately in the external
install receipt and work/stratus-170-rc5 evidence. Pending work stays pending.
''')
(p/'VALIDATION.txt').write_text('''Stratus 1.7.0-rc5 candidate; evidence: work/stratus-170-rc5.
Final native compatibility-shim compilation covers 768 program pairs across
8 variants; results are in compile-final.log. This is not Iris integration.
Targeted actual GLSL GPU checks compare hinted/fresh reflection RGBA across
planar, foreground, missing and cutout receivers and valid/invalid seeds;
refraction UVs against all selected guards at quality 0/1/2; and RG16F history
headers for consecutive, stale, first/slow and wrapped frames. Counts and
results are in optics-checks-final.json. Instrumented read counts are not
GPU timings or gameplay FPS. Deliberately wrong hints may increase reads.
Control audit preserves all 67 prior defaults/ranges/preset assignments and
620 block tokens, checks all 68 options reachable with labels/tooltips.
Actual installer policy tests run in temporary profiles. No override resets.

Development QA-v1 On loaded in the actual Main/Iris pipeline. One 1440x842
normal-world river view was captured/reviewed after a stable 5124ms gate,
441/441 disk columns and no mesh jobs/workers/uploads/tasks pending. Actual
probe was unfocused with Dynamic FPS capped at 1 FPS; slow-frame rejection
means this is not proof of effective temporal hint reuse or motion safety.
The Mac was reported locked. Test driver stopped and original rc3 selection,
HUD/pause/menu restored. Final candidate runtime evidence is external to this
immutable archive. Focused FPS, motion/disocclusion/glass/waterline/resize/
reload and representative matched On/Off acceptance remain required. No
performance gain or full all-reflections/refractions completion is claimed.
''')
(p/'IN-GAME-TEST.txt').write_text('''Compare final candidate TEMPORAL_OPTICS=0/1 and rc4 at identical saved quality,
framebuffer/render distance, camera, time and weather. Verify selected ZIP,
68 effective controls and all four actual Iris profiles. Confirm native RG16F
history targets and adjacent-frame stamps, then test water waves/shorelines,
waterfall, moving camera/disocclusion, reflected moving objects, glass/stacked
transparency, underwater exit, zero optics, reload and viewport changes.
Do not infer temporal hits from a slow/background screenshot; hints reject
frames over 50ms. Inspect representative matched frames and motion.

User has resumed focused FPS testing. Require real focus, active Dynamic FPS
and Minecraft inactivity limiter state, stable five-second loaded-column and
mesh gates and a fresh gate at sampling start. Compare repeated matched On/
Off samples with frame-time distributions, and Reference separately from the
user's manual full scenery reflections. Optional bounded activity timer must
stop afterwards. No quality/resolution/draw-distance reduction for speed.
Restore exact original settings/menu/camera only if no newer navigation was
made; preserve newer user changes. Stop helpers and remove only unchanged QA
files owned by this pass. Keep unverified requests in the active batch.
''')
