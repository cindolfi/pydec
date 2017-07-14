"Finite Element matrix creation"

from .info import __doc__

from .innerproduct import *

__all__ = [s for s in dir() if not s.startswith('_')]

