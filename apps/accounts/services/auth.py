from rest_framework_simplejwt.tokens import RefreshToken
from apps.core_logging.services import log_event
from apps.core_logging.constants import LogAction
from apps.accounts.services.tokens import create_tokens


def login_user(user) -> dict:
    """
    Generate JWT tokens for authenticated user.
    """

    log_event(
        action=LogAction.LOGIN,
        message="User logged in.",
        user=user,
    )
    return create_tokens(user)


def logout_user(*, user, refresh_token: str) -> None:
    """
    Blacklist refresh token.
    """
  
    log_event(
        action=LogAction.LOGOUT,
        message="User logged out.",
        user=user,
    )
    RefreshToken(refresh_token).blacklist()