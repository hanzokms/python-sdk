from hanzo_kms.kms_requests import KMSRequests
from hanzo_kms.resources.auth_methods import AWSAuth
from hanzo_kms.resources.auth_methods import UniversalAuth
from hanzo_kms.resources.auth_methods import OidcAuth
from hanzo_kms.resources.auth_methods import TokenAuth
from hanzo_kms.resources.auth_methods import LdapAuth
from typing import Callable

class Auth:
    def __init__(self, requests: KMSRequests, setToken: Callable[[str], None]):
        self.requests = requests
        self.aws_auth = AWSAuth(requests, setToken)
        self.universal_auth = UniversalAuth(requests, setToken)
        self.oidc_auth = OidcAuth(requests, setToken)
        self.token_auth = TokenAuth(setToken)
        self.ldap_auth = LdapAuth(requests, setToken)
