# Stratus — changes for the next coding pass

Put only the changes you want worked on now under **Pending changes**. `TASK.md` is the complete shader target and remains in force for everything else. A saved file does not start work; tell the coding chat **“Apply the pending changes.”** After implementation and verification, move completed requests to [COMPLETED-CHANGES.md](COMPLETED-CHANGES.md) with the release/evidence reference. If none remain pending, leave **“No pending changes.”** Partial or unverified work stays pending. Studio run actions save the submitted brief as a separate `IN-PROGRESS/<request-id>/CHANGES.md` batch and clear this pending section for your next requests. The coder works on that saved batch; queued work is not completed work.

## Pending changes

- [ ] Complete efficient temporal optimisation across **all reflections and refractions**, preserving sharp current colour, correct occlusion/motion, all controls and selected sampling/resolution. Rc5 adds optional prior-frame intersection hints for water/glass scenery searches and prior shoreline-rejection ordering for water refraction, but this is only a default-off experiment. Six matched focused samples show no speedup (manual On about3% slower; Reference difference under1%). Cheap sky lookup, thin-glass refraction and the straight underwater exit remain fresh. Deliver a net-efficient approach; keep the approximately60FPS Reference goal pending. Continuous motion/disocclusion, glass/layering, waterline, reload/viewport and full-path acceptance remain unverified.

## Progress and evidence

- Focused FPS comparison itself is complete and moved to COMPLETED-CHANGES.md; that does not complete the optimisation request above. Six accepted primary20-second samples at1440×842, real focus, stable441/441-column/zero-mesh gates, documented active limiter/quality. No visual-quality reductions or supported speedup claim.
- Candidate `outputs/Stratus-1.7.0-rc5.zip` installed and actually loaded; source/archive/install match.68 controls/four actual Iris profiles,768 native pairs, targeted GPU cases at all three refraction qualities and17 migration checks pass.
- Details: `work/stratus-170-rc5/performance-results.json`, `final-audit.json`, `optics-checks-final.json`, nine reviewed river captures and CHANGE-LOG.md26October2026 rc5 entry.
- Per-pass GPU profiling could not initialise under Fabric class-loader visibility checks, before transformer registration; no timings or active hook claimed. Use a supported profiling integration for deeper bottleneck work.
- Original rc3 selection/config/HUD/pause/options restored; newer user camera angle preserved; helpers stopped and owned QA files removed. No fixtures/world blocks changed. Shared next queue, immutable batch target and frozen bridge snapshots untouched.
- Frozen TASK delta only repeated completed rc4 material/evidence reconciliation; no new material work staged. No newer document conflict found.
