from oauthlib.common import extract_params
from oauthlib.oauth1 import Client, SIGNATURE_HMAC, SIGNATURE_TYPE_AUTH_HEADER
from oauthlib.oauth1 import SIGNATURE_TYPE_BODY


DEFAULT_HTTP_CONTENT_TYPE = "application/octet-stream"
CONTENT_TYPE_MULTI_PART = 'multipart/form-data'

class OAuth1:
    
    client = Client
    
    def __init__(self,client_key,client_secret=None,
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
        self.app = app
        self.session_interface = session_interface
        
    def __getClient__()