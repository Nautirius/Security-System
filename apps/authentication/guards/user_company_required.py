from functools import wraps

from django.http import HttpResponseForbidden
from django.shortcuts import redirect

from apps.buildings.models import Company


def user_company_required(company_lookup_field='id', param_name='company_id'):
    """
        Dekorator sprawdzający, czy użytkownik ma dostęp do firmy.

        :param company_lookup_field: Pole, według którego będzie wyszukiwane (np. 'id', 'name').
        :param param_name: Nazwa parametru przekazywanego do widoku (np. 'company_id', 'company_name').
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):

            company_value = kwargs.get(param_name)

            if not company_value:
                return HttpResponseForbidden("Missing company identifier")

            try:
                company = Company.objects.get(**{company_lookup_field: company_value})
            except Company.DoesNotExist:
                return HttpResponseForbidden("Company does not exist")

            user_profile = getattr(request.user, 'profile', None)
            if not user_profile or not user_profile.companies.filter(pk=company.pk).exists():
                return HttpResponseForbidden("User has no access for this company")

            request.company = company

            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
