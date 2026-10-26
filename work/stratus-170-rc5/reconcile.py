from pathlib import Path
import hashlib,json,re,shutil
root=Path.cwd();w=root/'work/stratus-170-rc5';docs=root/'work/Custom instructions';batch=docs/'IN-PROGRESS/c3ec7834-5d1e-403e-9eb7-7a12a3226909';initial=json.loads((w/'initial-fingerprints.json').read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
# Re-read all current applicable documents immediately before focused edits.
target=docs/'TASK.md';task=target.read_text();brief=(batch/'CHANGES.md').read_text();log=(docs/'CHANGE-LOG.md').read_text();archive=(docs/'COMPLETED-CHANGES.md').read_text();shared=docs/'CHANGES.md';conflicts=[]
if sha(target)!=initial['work/Custom instructions/TASK.md']:conflicts.append('Shared TASK has newer edits; only exact unchanged targeted lines may be reconciled.')
if sha(shared)!=initial['work/Custom instructions/CHANGES.md']:conflicts.append('Shared next queue has newer edits; preserved entirely.')
for n,p in [('TASK.md',target),('CHANGES.md',batch/'CHANGES.md'),('CHANGE-LOG.md',docs/'CHANGE-LOG.md'),('COMPLETED-CHANGES.md',docs/'COMPLETED-CHANGES.md')]:shutil.copy2(p,w/('pre-reconcile-'+n))
# Batch template guard preserves unexpected newer active-brief edits.
stage=(w/'stage.py').read_text();template=re.search(r"p.write_text\(head\+'''(.*?)'''\)",stage,re.S)[1];expected=(w/'batch-CHANGES.md').read_text().split('## Pending changes')[0]+template
if brief!=expected:raise RuntimeError('Newer active batch brief differs; review before reconciliation')
new_current='- Current editable source = `outputs/Stratus/`, packaged as `outputs/Stratus-1.7.0-rc5.zip` for batch `c3ec7834-5d1e-403e-9eb7-7a12a3226909`. Experimental temporal optics intersection/shoreline hints are optional and default off. All prior67 controls/defaults/ranges/preset assignments remain;68 total. Exact final ZIP/source/install and actual Iris options/four profiles verified. Six focused20-second comparisons show no speedup: manual full-scenery reflections about31FPS Off/30FPS On; complete Reference about50.2Off/49.9On at1440×842. Keep all-optics temporal coverage, net optimisation and broader motion acceptance pending in this batch. Earlier waterline/leaf-cluster work remains in its earlier batches. This is not full1.7 milestone acceptance.'
lines=task.splitlines();baseline=(w/'batch-TASK.md').read_text().splitlines()
old_current=next(l for l in baseline if l.startswith('- Current editable source ='))
if old_current in lines:lines[lines.index(old_current)]=new_current
else:conflicts.append('Current-source paragraph changed; preserved newer wording instead of replacing.')
optics='- Optics temporal optimisation = extend temporal optimisation across all reflections and refractions while retaining current quality, controls, sharp colour, correct occlusion and motion. Current rc5 only provides experimental prior-frame distance seeds for water/glass scenery searches and previous rejected shoreline-guard ordering for water refraction; every accepted hit/colour is current-frame. It has no colour-history accumulation and does not skip renderer frames. Cheap sky lookup, thin-glass refraction and the unbent underwater exit remain fresh. Source/GPU/finite river checks do not complete the full request. Measured On adds cost in the manual river scene, so default Off in all presets until a net-efficient implementation and full live acceptance are established.'
if not any(l.startswith('- Optics temporal optimisation =') for l in lines):
 idx=next(i for i,l in enumerate(lines) if l.startswith('- Temporal optimisation ='));lines.insert(idx+1,optics)
old_latest=next(l for l in baseline if l.startswith('- Latest candidate evidence ='))
if old_latest in lines:lines[lines.index(old_latest)]=old_latest.replace('- Latest candidate evidence =','- Previous material-candidate evidence (rc4) =',1)
new_latest='- Latest candidate evidence = rc5 passes768 native program pairs;960 reflection cases,1344 refraction cases at each of three quality levels, and eight RG16F history checks per run, with zero failures/API errors and tested RGBA/UV parity.17 real installer tests pass; all68 options reachable, all old67 defaults/ranges/preset assignments and620 block tokens retained. Exact final ZIP loaded with saved overrides, all four68-option Iris profiles match. Nine river captures inspected; six primary focused20-second samples pass stable441/441-column/zero-mesh-work gates. Manual matched pairs show On about3% slower; strict Reference50.24Off/49.91On, no supported gain or60FPS acceptance. Saved VSync=true; DynamicFPS reports enableVsync=false, effective swap interval not independently verified. Sampling checks real focus, NONE inactivity limiter/cap70 and DynamicFPS FOCUSED/idlefalse; strict Reference has zero bad limiter polls. All QA helpers stopped, owned temporary files removed, original rc3/config/HUD/pause/flight restored; newer user camera angle preserved. Per-pass profiler could not initialise under Fabric class-loader visibility checks; no timing/hook claim. See CHANGE-LOG.md and `work/stratus-170-rc5/performance-results.json`.'
idx=next(i for i,l in enumerate(lines) if l.startswith('- Previous material-candidate evidence (rc4) ='));lines.insert(idx,new_latest)
# Shared next queue and immutable snapshots never written.
if target.read_text()!=task:raise RuntimeError('TASK changed during reconciliation; retry focused merge')
target.write_text('\n'.join(lines)+'\n')
entry='''## 26 October 2026 — Stratus 1.7.0-rc5 — experimental temporal optics hints

### At a glance

- Optional **Temporal optics hints**, default **Off**, adds prior-frame geometry/search hints for water/glass scenery reflections and water shoreline refraction checks. Fresh depth, occlusion and colour remain; no renderer frame skipping or colour accumulation. **The full all-reflections/refractions optimisation request remains pending.**
- [Candidate ZIP](../../outputs/Stratus-1.7.0-rc5.zip), [install/load receipt](../../outputs/Stratus-1.7.0-rc5-install.json), [nine reviewed finite river captures](../../outputs/Stratus-1.7.0-rc5-visual-checks/index.html). Exact final source/archive/install bytes match;250 entries,7,785,718bytes;SHA256 `4424a2f229ffca4519e0b619264b933de44b3f365532246492ad6b2fa68632d0`.
-768 native pairs, targeted GPU comparisons at all three refraction qualities,17 installer checks,68 reachable options and four actual68-option Iris profiles pass. All previous67 option defaults/ranges/preset assignments and620 block tokens retained. **Six valid focused FPS samples now recorded; no speedup.** Keep this experiment disabled. Net optimisation, approximately60FPS Reference goal and broad motion/glass/waterline acceptance remain pending.

Batch: [c3ec7834 active brief](IN-PROGRESS/c3ec7834-5d1e-403e-9eb7-7a12a3226909/CHANGES.md). Frozen delta repeats completed rc4 material reconciliation, so no duplicate material work. Shared next queue, immutable batch target and frozen snapshots are preserved. Only this batch's brief is staged/reconciled; earlier pending batches remain untouched. No newer document conflict was found before reconciliation.

### Implementation and technical evidence

Eleven shader files listed in `work/stratus-170-rc5/source-changes.json`, with exact `changes.diff`. New `temporal-optics.glsl` retains only the immediately preceding distance/rejected-step hint, frame stamps and slow-frame rejection. Water reflection and transparent-solid scenery searches validate a current receiver plane from the hint, then retain current foreground traversal and selected ray budgets. A failed seed falls back to the original search. Water refraction may test its prior rejected guard first using current depth; all accepted rays still evaluate the full chosen guard set. Cheap sky/environment lookups, thin-glass single-guard refraction and the straight underwater exit remain fresh. This is partial temporal search acceleration, not a claim of full radiance-history coverage or final optimisation success.

No new pass, reduced resolution, smaller ray budget, draw-distance change or deleted control. Optional On uses up to three RG16F ping-pong histories in existing passes, following their existing resolutions; unused scenery/quality-zero targets are conditional. At1440×842/full scenery/half water, raw paired storage is about21.8MB before driver overhead. Extra writes and invalid hints can cost more than saved reads, which is why the measured experiment remains default Off in all presets.

`compile-final.log`:768 final native compatibility-shim program pairs, zero failures (not a Minecraft emulator). `optics-checks-final.json`:960 reflection comparisons across planar/foreground/missing/cutout data and valid/invalid seeds;1344 UV comparisons at each refraction quality0/1/2; eight RG16F consecutive/stale/first/slow/wrapped-history checks per run. Tested reflection RGBA error0, matching refraction UVs, zero failures/API errors. Instrumented valid-seed receiver reads3620→3597; quality2 refraction reads598→559. These are finite synthetic read counts, not GPU timings or gameplay speedup; deliberately wrong seeds add work. `control-checks.json`, `migration-checks.json` and `final-release-runtime.json` record full control/menu/preset/migration checks. Final actual Iris load verifies all68 effective options, saved overrides and four complete68-option profiles. No override reset. Rc4 ZIP remains byte-identical. Packaged CHECKS/VALIDATION are pre-live-test snapshots; external receipt and this entry carry subsequent runtime/FPS evidence without rewriting the immutable ZIP.

Primary design references: [Iris ColorTex lifetime/ping-pong and32-buffer support](https://shaders.properties/current/reference/buffers/colortex/) and [GPUOpen temporal denoising/disocclusion discussion](https://gpuopen.com/manuals/fidelityfx_sdk/techniques/denoiser/). No third-party shader implementation copied. Current code validates fresh geometry instead of assuming previous reflected radiance stays valid as waves or objects move.

### Focused performance and finite visual review

Actual Main/Stratus Terrain Lab, Apple M1, OpenGL4.1 Metal91.7,1440×842, render distance12/simulation8, time1000/rain0. Saved VSync=true; DynamicFPS reports enableVsync=false, effective swap interval not independently queried. Matched user-setting comparisons, not uncapped GPU-throughput certification. DynamicFPS stays enabled/FOCUSED/idlefalse; actual Minecraft limiter is NONE with cap70 during accepted sampling. The initial SHORT_AFK30FPS cap was cleared by bounded timer activity, without saved-setting changes or fake focus. All primary samples are20seconds, real focus throughout, fixed camera/framebuffer,441/441 disk columns, stable counts at least5seconds and zero queued jobs/busy workers/uploads/task lists. Fresh gate at start and continued loading/camera/focus/size guards pass.

| Matched pair | Off FPS | On FPS | On relative change | Off/On median ms | Off/On p95 ms |
|---|---:|---:|---:|---:|---:|
| Manual A |31.4156|30.4226|−3.16%|31.7145 /33.0758|41.3527 /43.6683|
| Manual B, reverse order |30.9330|30.0311|−2.92%|32.2960 /33.1093|43.3888 /46.2996|
| Complete Reference, strict limiter checks |50.2411|49.9118|−0.66%|19.7030 /19.8241|26.4176 /25.5165|

Manual uses saved full scenery mode2, waterstyle0, half water/atmosphere and refraction1, turbidity0.50/visibility6. Reference applies all68 source profile values, including sky-only reflections and native water; it is a separate baseline, not a constant-quality gain over manual. User changed camera between A and B; pairs each match, and Reference uses B's view. The newer angle is preserved. Two preliminary Reference samples (~51.8/~51.6FPS) remain as secondary evidence only: the standalone activity helper expired near their end, so the pair was rerun with sample-bound activity and per-poll limiter/DynamicFPS checks; zero bad polls. Raw frame times, gates, active-monitor metadata, exact options and qualification details live in `work/stratus-170-rc5/benchmarks/`, `activity-monitor.txt`, `bench-runtime-*.txt` and `performance-results.json`.

Nine unedited actual captures were inspected, including final-byte manual/Reference On/Off variants. No obvious water rectangles, stale-colour accumulation or broken river composition seen in this finite coverage. Animated waves/textures/clouds/particles vary naturally. One earlier QA-v1 screenshot was unfocused1FPS and proves neither temporal reuse nor motion safety. Continuous motion/disocclusion, glass/layering, waterline, resize/reload and all-path acceptance are still pending. Gallery images/links/hashes checked; gallery HTML was not separately browser-rendered. Per-pass GPU-query profiling was attempted, but Fabric refused access to the unexposed helper class before any transformer registration. No per-pass timings or successful hook claimed; no persistent instrumentation installed.

### Restoration and remaining work

Original rc3 enabled selection/config, HUD/pause/menu, flight, saved options, weather/time and all saved override values restored/retained. The user moved the view between test pairs; that newer angle was preserved instead of resetting the old one. Iris updated timestamp comments only in the original settings file. Helpers stopped;12 owned temporary QA files removed or automatically discarded by Iris after effective-option equality checks; no fixtures/world blocks changed. Final candidate stays installed alongside preserved old releases. `final-audit.json` checks exact source/archive/install equivalence, loaded options/profiles, restoration and cleanup.

Focused comparison is complete and archived as verification only. The all-optics temporal optimisation request remains pending because this hint approach provides no measured benefit and does not cover full temporal colour reuse. Next work is a more effective design with motion/disocclusion validity and practical profiling through a supported integration, followed by matched active-game acceptance at unchanged quality. Do not enable/promote this prototype as a performance improvement or mark the full batch complete.

'''
(docs/'CHANGE-LOG.md').write_text(log.replace('# Stratus change and output log\n','# Stratus change and output log\n\n'+entry,1))
completed='''### Stratus1.7.0-rc5 — 26 October 2026 — batchc3ec7834 — focused comparison only

- [x] Requested focused active-game comparison completed: six primary20-second samples,1440×842, Apple M1, actual focus/throttling/activity and loaded-column/mesh gates recorded. Two matched manual pairs (~31.4Off/30.4On and30.9Off/30.0On) and a separate strict Reference pair (50.24Off/49.91On) show no supported gain. All quality choices preserved; no60FPS acceptance. Nine finite river captures inspected. Original shader/config/options/HUD/pause restored, newer camera angle preserved and helpers/owned QA files cleaned up.

This archives the **measurement**, not the full optimisation request. Effective all-reflections/refractions temporal work, net performance improvement and broader live motion acceptance remain pending in the active batch. [Evidence and limitations](CHANGE-LOG.md#26-october-2026--stratus-170-rc5--experimental-temporal-optics-hints) · [Raw comparison report](../../work/stratus-170-rc5/performance-results.json) · [Candidate](../../outputs/Stratus-1.7.0-rc5.zip).

'''
(docs/'COMPLETED-CHANGES.md').write_text(archive.replace('## Completed changes\n','## Completed changes\n\n'+completed,1))
head=brief.split('## Pending changes')[0]
(batch/'CHANGES.md').write_text(head+'''## Pending changes

- [ ] Complete efficient temporal optimisation across **all reflections and refractions**, preserving sharp current colour, correct occlusion/motion, all controls and selected sampling/resolution. Rc5 adds optional prior-frame intersection hints for water/glass scenery searches and prior shoreline-rejection ordering for water refraction, but this is only a default-off experiment. Six matched focused samples show no speedup (manual On about3% slower; Reference difference under1%). Cheap sky lookup, thin-glass refraction and the straight underwater exit remain fresh. Deliver a net-efficient approach; keep the approximately60FPS Reference goal pending. Continuous motion/disocclusion, glass/layering, waterline, reload/viewport and full-path acceptance remain unverified.

## Progress and evidence

- Focused FPS comparison itself is complete and moved to COMPLETED-CHANGES.md; that does not complete the optimisation request above. Six accepted primary20-second samples at1440×842, real focus, stable441/441-column/zero-mesh gates, documented active limiter/quality. No visual-quality reductions or supported speedup claim.
- Candidate `outputs/Stratus-1.7.0-rc5.zip` installed and actually loaded; source/archive/install match.68 controls/four actual Iris profiles,768 native pairs, targeted GPU cases at all three refraction qualities and17 migration checks pass.
- Details: `work/stratus-170-rc5/performance-results.json`, `final-audit.json`, `optics-checks-final.json`, nine reviewed river captures and CHANGE-LOG.md26October2026 rc5 entry.
- Per-pass GPU profiling could not initialise under Fabric class-loader visibility checks, before transformer registration; no timings or active hook claimed. Use a supported profiling integration for deeper bottleneck work.
- Original rc3 selection/config/HUD/pause/options restored; newer user camera angle preserved; helpers stopped and owned QA files removed. No fixtures/world blocks changed. Shared next queue, immutable batch target and frozen bridge snapshots untouched.
- Frozen TASK delta only repeated completed rc4 material/evidence reconciliation; no new material work staged. No newer document conflict found.
''')
checkpoint='''# Batch progress

Status: partial — candidate built/tested; effective all-optics optimisation remains pending

## Resume here
- Active brief: this batch's CHANGES.md only. Shared CHANGES.md is protected next unsent work.
- Source/package: `outputs/Stratus`, immutable `outputs/Stratus-1.7.0-rc5.zip`, SHA2564424a2f229ffca4519e0b619264b933de44b3f365532246492ad6b2fa68632d0.250 entries,7,785,718bytes. Source/archive/install match.
- Current shader selection restored to rc3 enabled. Final HUD/pause/menu/flight/options unchanged, newer user camera yaw−67.70922/pitch10.483427 preserved. Helpers stopped; all owned QA files cleaned up. No world-block mutation.
- Next concrete work: develop an effective all-optics temporal design with correct motion/disocclusion and fresh fallback, or obtain supported pass profiling; current hint approach is not faster. Keep TEMPORAL_OPTICS0/default Off. No lowering quality or claiming60FPS.

## Evidence and remaining work
-768 native compile/link pairs pass: `work/stratus-170-rc5/compile-final.log`.
- GPU:960 reflection comparisons,1344 refraction comparisons for each quality0/1/2,8 RG16F history cases per run; no failures/API errors or tested colour/UV mismatch. `optics-checks-final.json`.
- All old67 defaults/ranges/presets and620 block tokens retained;68 controls reachable.17 actual installer checks pass. Exact final ZIP loaded; four actual68-option Iris profiles match, saved overrides retained. `control-checks.json`, `migration-checks.json`, `final-release-runtime.json`, `final-audit.json`.
- Six primary focused20s samples,1440×842, Apple M1, render distance12, time1000/rain0, real focus, stable441-column/zero-mesh gates. Manual A31.42Off/30.42On; manual B30.93Off/30.03On. Strict Reference50.24Off/49.91On with zero limiter/DynamicFPS violations, cap70. SavedVSync=true, DynamicFPS reportsVSyncfalse; effective swap interval not independently checked. No supported gain. `performance-results.json`, raw `benchmarks/`, `activity-monitor.txt`.
- Nine finite river captures inspected. Continuous motion/glass/waterline/reload/resize/full temporal optics coverage remain pending. Earlier unrelated batches untouched.
- Four-second per-pass query helper failed Fabric class-loader visibility check before registering any transformer; no accepted pass timings/hook. `gpu-profiling-blocker.json`.
- Shared TASK reconciled carefully; focused comparison archived separately from pending optimisation. Package CHECKS/VALIDATION are pre-live-test snapshots; external receipt/log contain subsequent evidence. No newer document conflict found.
'''
(batch/'PROGRESS.md').write_text(checkpoint)
(w/'reconciliation.json').write_text(json.dumps({'conflicts':conflicts,'shared_next_queue_unchanged_by_coder':True,'pending_requests':1,'archived_completed_measurement_only':True,'batch_target_sha256':sha(batch/'TASK.md'),'shared_next_queue_sha256':sha(shared),'shared_TASK_after_sha256':sha(target)},indent=2)+'\n')
print('Reconciled pending optimisation and archived focused measurement only; conflicts:',conflicts)
