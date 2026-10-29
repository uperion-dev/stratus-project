# Batch progress

Status: rc8 source candidate implemented; acceptance pending.

- Frozen delta reviewed/staged: existing rc7 restoration preserved. Shared queue and target unchanged.
- Changes: 1.3.1 RGB face formula with retained controls; native model lighting now covers block entities/hand; shared water-optics library and fused composition selector; prior Layered renderer retained.
- 768 native program pairs passed before the final FACE_BLEND bypass refinement; rerun final checks. GPU 144 face/entity cases pass, archived-reference RGB error0.
- Remaining: final compile/control/migration/GPU water checks, actual Main entity/hand/waterline/underwater visual comparisons, matched focused FPS against actual1.3.1. Do not claim speedup/parity.
- Evidence: work/stratus-170-rc8. Resume with final tests and Main QA. All five requests remain pending acceptance in this brief.
