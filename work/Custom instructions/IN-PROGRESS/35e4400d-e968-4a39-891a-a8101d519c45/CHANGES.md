# Stratus — changes for the next coding pass

Put only the changes you want worked on now under **Pending changes**. `TASK.md` is the complete shader target and remains in force for everything else. A saved file does not start work; tell the coding chat **“Apply the pending changes.”** After implementation and verification, move completed requests to [COMPLETED-CHANGES.md](COMPLETED-CHANGES.md) with the release/evidence reference. If none remain pending, leave **“No pending changes.”** Partial or unverified work stays pending. Studio run actions save the submitted brief as a separate `IN-PROGRESS/<request-id>/CHANGES.md` batch and clear this pending section for your next requests. The coder works on that saved batch; queued work is not completed work.

## Pending changes

- Use the 1.3.1 realistic face shading to replace the current realistic face shading. 

- Fix all entity face shadings. Currently theres no shading on some entities eg. block and player hand. 

- Get a hint for 1.3.1 under water, water surface for consistancy with the top surface. 

- Use 1.3.1 super fast water render. 

- Achive 1.3.1 FPS performance. 


## Frozen delta staging

The meaningful rc7 delta is already implemented in the starting source: Classic reflection/wet-film selectors and independent native-emitter bloom. It is preserved, not rebuilt. Its historical full-optics temporal and final rc7 FPS caveats remain with their original batches; this batch specifically requests an actual 1.3.1 performance comparison. No formatting-only changes were staged.

## Technical candidate checkpoint — 30 October 2026

The five requests above remain pending acceptance. Candidate1.7.0-rc8 restores the archived RGB face response, extends native model-lighting coverage and adds a selectable fused composition path while preserving current underwater-exit/transparent protections. Technical checks pass; underwater/top appearance and actual1.3.1 FPS are unverified. The user requested technical checks only for now. See [PROGRESS.md](PROGRESS.md), `work/stratus-170-rc8/final-audit.json` and the rc8 CHANGE-LOG entry. Shared next queue untouched.
