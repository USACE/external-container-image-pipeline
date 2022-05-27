import os

# NOTE: Environment Variables intentionally not prefixed with PGADMIN_CONFIG_* to avoid
#       conflicting with default behavior of pgadmin4 docker container

OAUTH2_AUTO_CREATE_USER = True

OAUTH2_CONFIG = [
    {
        # The name of the of the oauth provider, ex: github, google
        'OAUTH2_NAME': os.getenv('OAUTH2_NAME'),
        # The display name, ex: Google
        'OAUTH2_DISPLAY_NAME': os.getenv('OAUTH2_DISPLAY_NAME', '<Oauth2 Display Name>'),
        # Oauth client id
        'OAUTH2_CLIENT_ID': os.getenv('OAUTH2_CLIENT_ID'),
        # Oauth secret
        'OAUTH2_CLIENT_SECRET': os.getenv('OAUTH2_CLIENT_SECRET'),
        # URL to generate a token,
        # Ex: https://github.com/login/oauth/access_token
        'OAUTH2_TOKEN_URL': os.getenv('OAUTH2_TOKEN_URL'),
        # URL is used for authentication,
        # Ex: https://github.com/login/oauth/authorize
        'OAUTH2_AUTHORIZATION_URL': os.getenv('OAUTH2_AUTHORIZATION_URL'),
        # Oauth base url, ex: https://api.github.com/
        'OAUTH2_API_BASE_URL': os.getenv('OAUTH2_API_BASE_URL'),
        # Name of the Endpoint, ex: user
        'OAUTH2_USERINFO_ENDPOINT': os.getenv('OAUTH2_USERINFO_ENDPOINT'),
        # Oauth scope, ex: 'openid email profile'
        # Note that an 'email' claim is required in the resulting profile
        'OAUTH2_SCOPE': os.getenv('OAUTH2_USERINFO_ENDPOINT'),
        # Font-awesome icon, ex: fa-github
        'OAUTH2_ICON': os.getenv('OAUTH2_ICON'),
        # UI button colour, ex: #0000ff
        'OAUTH2_BUTTON_COLOR': os.getenv('OAUTH2_BUTTON_COLOR'),
    }
]
