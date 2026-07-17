from rest_framework_simplejwt.tokens import RefreshToken

from apps.accounts.services.tokens import create_tokens


def login_user(user) -> dict:
    """
    Generate JWT tokens for authenticated user.
    """

    return create_tokens(user)


def logout_user(refresh_token: str) -> None:
    """
    Blacklist refresh token.
    """

    RefreshToken(refresh_token).blacklist()