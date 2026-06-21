# Hanzo KMS Python SDK

Official Python SDK for [Hanzo KMS](https://kms.hanzo.ai) -- secrets management, encryption keys, and dynamic secrets.

## Installation

```bash
pip install hanzo-kms
```

## Quick Start

```python
from hanzo_kms import KMSClient

# Initialize the client
client = KMSClient(host="https://kms.hanzo.ai")

# Authenticate with Universal Auth
client.auth.universal_auth.login(
    client_id="your-client-id",
    client_secret="your-client-secret"
)

# List secrets
secrets = client.secrets.list_secrets(
    project_id="your-project-id",
    environment_slug="production",
    secret_path="/"
)

for secret in secrets.secrets:
    print(f"{secret.secretKey}={secret.secretValue}")
```

## Authentication Methods

- **Universal Auth** -- Machine identity client ID/secret
- **Token Auth** -- Direct token authentication
- **AWS IAM Auth** -- AWS IAM-based authentication
- **OIDC Auth** -- OpenID Connect authentication
- **LDAP Auth** -- LDAP username/password authentication

## Features

- **Secrets** -- CRUD operations on secrets with caching support
- **KMS Keys** -- Create, manage, encrypt/decrypt with symmetric keys
- **Folders** -- Organize secrets into folder hierarchies
- **Dynamic Secrets** -- Provision short-lived credentials (databases, cloud providers, etc.)

## Caching

The SDK includes built-in secrets caching with configurable TTL:

```python
# Enable caching with 60-second TTL (default)
client = KMSClient(host="https://kms.hanzo.ai", cache_ttl=60)

# Disable caching
client = KMSClient(host="https://kms.hanzo.ai", cache_ttl=None)
```

## Context Manager

```python
with KMSClient(host="https://kms.hanzo.ai", token="your-token") as client:
    secrets = client.secrets.list_secrets(
        project_id="your-project-id",
        environment_slug="dev",
        secret_path="/"
    )
# Resources automatically cleaned up
```

## License

BSD-3-Clause -- Copyright (c) 2025-2026 Hanzo AI, Inc. See [LICENSE](LICENSE) and [NOTICE](NOTICE).

## Security

If you discover a security vulnerability, please report it to security@hanzo.ai. Do not file public issues for security vulnerabilities.
