"PyDEC meshes"

from .info import __doc__

from .simplex import *
from .regular_cube import *
from .generation import *
from .subdivision import *
from .ncube import *

__all__ = [s for s in dir() if not s.startswith('_')]

from pydec.testing import Tester
test = Tester().test

