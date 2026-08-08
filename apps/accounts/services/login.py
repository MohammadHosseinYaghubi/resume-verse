from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from apps.accounts.audit import log_login_failed, log_login_success
from apps.accounts.services.tokens import (create_tokens)
from apps.accounts.utils.rate_limit import (check_login_rate_limit)
from apps.accounts.signals import user_logged_in
from apps.security.services import (is_login_locked,
                                    register_failed_login,
                                    clear_login_attempts,
)
from django.core.exceptions import PermissionDenied


def login_user(*, username, password, ip_address):

    check_login_rate_limit(identifier=ip_address)
    
    if is_login_locked(ip_address):
        raise PermissionDenied(
            "Too many login attempts.",
        )
        
    user = authenticate(username=username,
        password=password,
    )

    if user is None:

        log_login_failed(username=username,
            ip_address=ip_address,
        )
        register_failed_login(ip_address,)
        raise AuthenticationFailed("Invalid credentials.")

    log_login_success(user=user, ip_address=ip_address)
    
    clear_login_attempts(ip_address,)
    
    user_logged_in.send(
        sender=login_user,
        user=user,
        ip_address=ip_address,
    )
        
    return create_tokens(user)