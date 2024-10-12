from django.shortcuts import render

from common.models import QuestionModel, AboutModel
from users.models import TeamModel
from post.models import OfferModel


def home_page_view(request):
    teams = TeamModel.objects.all()
    three_offers = OfferModel.objects.filter(is_pinned=True)[:4]
    offers = OfferModel.objects.filter(is_pinned=True)[4:]
    questions = QuestionModel.objects.all()
    about = AboutModel.objects.last()

    context = {
        'teams': teams,
        'three_offers': three_offers,
        'offers': offers,
        'questions': questions,
        'about': about,
    }
    return render(request, 'index.html', context)