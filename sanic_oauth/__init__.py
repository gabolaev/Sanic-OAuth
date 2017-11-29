from .provider import *

__author__ = 'Shawn Niederriter'

__version__ = '0.0.5'

import logging
try:
    from logging import NullHandler
except ImportError:
   class NullHandler(logging.Handler):
       def emit(self, record):
           pass

logging.getLogger('sanic_oauth').addHandler(NullHandler())
