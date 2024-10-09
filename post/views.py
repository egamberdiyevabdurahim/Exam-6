from django.shortcuts import render, redirect

from post.form import OfferModelForm, ProblemModelForm
from post.models import ProblemModel, OfferModel


def create_offer_view(request):
    if request.method == 'POST':
        form = OfferModelForm(request.POST)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.user = request.user
            offer.save()
            return redirect('home')
        else:
            return render(request, 'forms/offer-form.html', {'form': form})
    return render(request, 'forms/offer-form.html')


def create_problem_view(request):
    if request.method == 'POST':
        form = ProblemModelForm(request.POST)
        if form.is_valid():
            problem = form.save(commit=False)
            # problem.user = request
            problem.save()
            return redirect('common:home')
        else:
            return render(request, 'forms/offer-form.html', {'form': form})
    return render(request, 'forms/offer-form.html')