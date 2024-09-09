__all__ = ["MalformedCoordinates", "NEVR", "NEVRA", "NVR", "NVRA"]

from ._exceptions import MalformedCoordinates
from .nvr import NEVR, NEVRA, NVR, NVRA

try:
    from .version import __version__
except ImportError:
    # version.py is generated at build time
    # if for some reason it's missing use the same fallback PDM uses
    __version__ = "0.0.0"
