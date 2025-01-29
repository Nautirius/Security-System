from functools import wraps

from django.http import HttpResponseForbidden
from django.shortcuts import redirect


def custom_permission_required(field_name, expected_value, redirect_url=None):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):

            if not request.user.is_authenticated:
                return redirect('account_login')

            user_profile = getattr(request.user, 'user_profile', None)
            if not user_profile or getattr(user_profile, field_name, None) != expected_value:
                if redirect_url:
                    return redirect(redirect_url)
                return HttpResponseForbidden("This user has no permission to this view in Security System panel")

            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
