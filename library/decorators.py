from functools import wraps
from django.contrib.auth.decorators import user_passes_test

def is_superuser(user):
    return user.is_authenticated and user.is_superuser

superuser_required = user_passes_test(is_superuser)