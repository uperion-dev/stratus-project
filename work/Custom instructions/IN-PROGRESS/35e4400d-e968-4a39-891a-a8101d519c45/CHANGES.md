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
