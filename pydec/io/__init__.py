"PyDEC mesh and array IO"

from .info import __doc__

from .meshio import *
from .arrayio import *

__all__ = [s for s in dir() if not s.startswith('_')]

