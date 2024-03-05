from flask_appbuilder.security.manager import AUTH_OAUTH
from aws_secrets_manager import SecretsManager

secret_manager = SecretsManager("prod/superset", "us-east-1")

SECRET_KEY = secret_manager.get_secret_value("SECRET_KEY")
client_id = secret_manager.get_secret_value("client_id")
client_secret = secret_manager.get_secret_value("client_secret")
server_metadata_url = secret_manager.get_secret_value("server_metadata_url")
access_token_url = secret_manager.get_secret_value("access_token_url")
authorize_url = secret_manager.get_secret_value("authorize_url")

AUTH_TYPE = AUTH_OAUTH
AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = "Admin"
OAUTH_PROVIDERS = [
    {
        'name': 'auth0',
        'icon': 'fa-google',
        'token_key': 'access_token',
        'remote_app': {
            'client_id': client_id,
            'client_secret': client_secret,
            'client_kwargs': {
                'scope': 'openid profile email',
            },
            'server_metadata_url': server_metadata_url,
            'access_token_url': access_token_url,
            'authorize_url': authorize_url,
        }
    }
]
