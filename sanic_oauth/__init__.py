from .oauth1_auth import OAuthInterface
#from .oauth2_auth import OAuth2Interface

__author__ = 'Shawn Niederriter'

__version__ = '0.0.2'

import logging
try:
    from logging import NullHandler
except ImportError:
   class NullHandler(logging.Handler):
       def emit(self, record):
           pass

logging.getLogger('sanic_oauth').addHandler(NullHandler())