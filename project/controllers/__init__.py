import os
import glob
__all__ = [os.path.basename(
    f)[:-3] for f in glob.glob(os.path.dirname(__file__) + "/*.py")]


from outlet_control import bp as outlet_bp
from printer import bp as hdmi_bp
