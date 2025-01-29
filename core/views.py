from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.shortcuts import render
from django.db.models import Q

from apps.authentication.models import UserProfile
from apps.buildings.models import Zone, Company, Building
from apps.cameras.models import Camera
from apps.permissions.models import Permission


@login_required
def full_text_search_view(request):
    query = request.GET.get("q", "")
    results = {}

    if query:
        search_query = SearchQuery(query)

        results['user_profiles'] = UserProfile.objects.annotate(
            search=SearchVector('first_name', 'last_name', 'email', 'phone', 'street', 'city', 'zip_code',
                                'companies__name'),
        ).filter(search=search_query)

        results['companies'] = Company.objects.annotate(
            search=SearchVector('name', 'buildings__label'),
        ).filter(search=search_query)

        results['permissions'] = Permission.objects.annotate(
            search=SearchVector('label'),
        ).filter(search=search_query)

        results['cameras'] = Camera.objects.annotate(
            search=SearchVector('label',  'zone__label', 'zone__building__label', 'zone__building__company__name'),
        ).filter(search=search_query)

        results['zones'] = Zone.objects.annotate(
            search=SearchVector('label', 'building__label', 'building__company__name'),
        ).filter(search=search_query)

        results['buildings'] = Building.objects.annotate(
            search=SearchVector('label', 'company__name', 'zones__label'),
        ).filter(search=search_query)

    return render(request, 'search.html', {'query': query, 'results': results})
