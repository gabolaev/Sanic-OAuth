from .oauth1_auth import OAuth1
from .oauth1_session import OAuth1Session
from .oauth2_auth import OAuth2
from .oauth2_session import OAuth2Session ##, TokenUpdated <-- Find out what this is

__author__ = 'Shawn Niederriter'

__version__ = '0.0.1'

import sanic
if sanic.__version__ < '0.4.1':
    msg = ('You are using Sanic version %s, which is older than '
           'Sanic-OAuth expects, please upgrade to 0.4.1 or later.')
    raise Warning(msg % sanic.__version__)

import logging
try:
    from logging import NullHandler
except ImportError:
   class NullHandler(logging.Handler):
       def emit(self, record):
           pass

logging.getLogger('sanic_oauth').addHandler(NullHandler())