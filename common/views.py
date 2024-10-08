from django.shortcuts import render

from users.models import TeamModel
from post.models import OfferModel


def home_page_view(request):
    teams = TeamModel.objects.all()
    offers = OfferModel.objects.filter(is_pinned=True)
    context = {
        'teams': teams,
        'offers': offers,
    }
    return render(request, 'index.html', context)