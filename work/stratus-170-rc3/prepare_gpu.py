from pathlib import Path
import sys,shutil
sys.path.insert(0,str(Path('work/stratus-check').resolve()));from prepare import expand,adapt,override
w=Path(__file__).parent;p=Path('outputs/Stratus/shaders').resolve();shutil.copy2('work/stratus-170-rc2/screen.vsh',w/'screen.vsh')
s='#version 330 compatibility\n#define DIMENSION_TYPE 0\n'+expand(p/'core/atmosphere.frag.glsl',p)
(w/'temporal.fsh').write_text(adapt(override(s,{'CLOUD_AMOUNT':'0.00','CIRRUS_AMOUNT':'0.00','MIST_AMOUNT':'0.00'}),'.fsh'))
