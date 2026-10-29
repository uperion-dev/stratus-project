Stratus 1.7.0-rc8 — candidate, visual/FPS verification pending
Restored the RGB hemisphere/key/indoor realistic face response from actual
Stratus 1.3.1 while retaining independent vanilla/realistic component controls.
Native model shading now includes block entities, held items and player hand.
Classic fused water composes optics at scene resolution in one pass as in
1.3.1; Layered retains selected optics-buffer resolution. Experimental temporal
hints select the Layered path. Existing current-frame transparency, native water
atlas/biome colour and nearest-exit underwater fog remain. No Snell window or
underwater reflection overlay is restored. This is not a wholesale old-pack
rollback. No 1.3.1 FPS parity or visual acceptance is claimed yet.
All prior 70 controls are retained; WATER_RENDERER adds a 71st control.
