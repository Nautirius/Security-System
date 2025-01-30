import logging
from typing import List
from functools import wraps

from django.http import HttpResponseForbidden
from django.shortcuts import render


def user_membership_role(roles: List[str]):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):

            user_profile = getattr(request.user, 'profile', None)
            if not user_profile:
                return render(
                    request,
                    '403.html',
                    context={"message": "No access: You dont have required privileges"},
                    status=403
                )

            memberships = user_profile.memberships.all()
            user_roles = [membership.role for membership in memberships]

            logging.info(f"User roles: {user_roles}")

            if not any(role in roles for role in user_roles):
                logging.warning("No Required Role. Breach attempt: {} ".format(user_profile.email))
                return render(
                    request,
                    '403.html',
                    context={"message": "No access: You dont have required privileges"},
                    status=403
                )

            return view_func(request, *args, **kwargs)

        return _wrapped_view
    return decorator
