from django.dispatch import Signal


user_registered = Signal()

user_logged_in = Signal()

user_logged_out = Signal()

password_changed = Signal()

password_reset_requested = Signal()

password_reset_completed = Signal()