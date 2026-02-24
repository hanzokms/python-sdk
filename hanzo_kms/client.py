from .kms_requests import KMSRequests

from hanzo_kms.resources import Auth
from hanzo_kms.resources import V3RawSecrets
from hanzo_kms.resources import KMS
from hanzo_kms.resources import V2Folders
from hanzo_kms.resources import DynamicSecrets

from hanzo_kms.util import SecretsCache

DEFAULT_HOST = "https://kms.hanzo.ai"

class KMSClient:
    def __init__(self, host: str = DEFAULT_HOST, token: str = None, cache_ttl: int = 60):
        """
        Initialize the Hanzo KMS client.

        :param str host: The host URL for your Hanzo KMS instance. Defaults to `https://kms.hanzo.ai`.
        :param str token: The authentication token for the client. If not specified, you can use the `auth` methods to authenticate.
        :param int cache_ttl: The time to live for the secrets cache in seconds. Set to `None` to disable caching. Defaults to `60` seconds.
        """

        self.host = host
        self.access_token = token

        self.api = KMSRequests(host=host, token=token)
        self.cache = SecretsCache(cache_ttl)
        self.auth = Auth(self.api, self.set_token)
        self.secrets = V3RawSecrets(self.api, self.cache)
        self.kms = KMS(self.api)
        self.folders = V2Folders(self.api)
        self.dynamic_secrets = DynamicSecrets(self.api)

    def set_token(self, token: str):
        """
        Set the access token for future requests.
        """
        self.api.set_token(token)
        self.access_token = token

    def get_token(self):
        """
        Get the access token for future requests.
        """
        return self.access_token

    def close(self):
        """
        Close the client and release resources.

        This stops the background cache cleanup thread. You don't need to call
        this if you're using the client as a context manager (with statement),
        as cleanup happens automatically when exiting the context.
        """
        if self.cache:
            self.cache.close()

    def __enter__(self) -> "KMSClient":
        """Support for context manager protocol."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Ensure cleanup when exiting context."""
        self.close()
