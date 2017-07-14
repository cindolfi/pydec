"""PyDEC: Software and Algorithms for Discrete Exterior Calculus
"""

from .version import version as __version__

from .dec import *
from .fem import *
from .math import *
from .io import *
from .mesh import *
from .util import *
from .vis import *

__all__ = [s for s in dir() if not s.startswith('_')]
__all__ += ['test', '__version__']

from pydec.testing import Tester
test = Tester().test
