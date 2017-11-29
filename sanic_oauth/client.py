from oauthlib.common import extract_params
from oauthlib.oauth1 import Client, SIGNATURE_HMAC, SIGNATURE_TYPE_AUTH_HEADER
from oauthlib.oauth1 import SIGNATURE_TYPE_BODY
from .provider import *


DEFAULT_HTTP_CONTENT_TYPE = 'application/octet-stream'
CONTENT_TYPE_MULTI_PART = 'multipart/form-data' 

class OAuthClient(object):
    
    def __init__(self,app):
        self.remote_apps = {}
        self.app = app
            
    def remote_app(self,name,provider,**kwargs):
        self.name = name
        if provider == 'airbnb':
            self.provider = Airbnb()
        elif provider == 'facebook':
            self.provider = Facebook()
        elif provider == 'google':
            self.provider = Google()
        elif provider == 'oauth1':
            self.provider = OAuth1()
        elif provider == 'oauth2':
            self.provider = OAuth2()
        else:
             self.provider = OAuthRemoteApp(self,**kwargs)
            
class OAuthRemoteApp(object):
    
    def __init__(self,client_key,auth_type,app=None,session_interface=None,client_secret=None,
            resource_owner_key=None,
            resource_owner_secret=None,
            callback_uri=None,
            signature_method=SIGNATURE_HMAC,
            signature_type=SIGNATURE_TYPE_AUTH_HEADER,
            rsa_key=None, verifier=None,
            decoding='utf-8',
            client_class=None,
            force_include_body=False,
            **kwargs):
        self.client = Client
        self.app = app
        self.client_key = client_key
        self.session_interface = session_interface
