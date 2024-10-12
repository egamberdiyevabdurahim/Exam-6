from itertools import chain

from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from common.templatetags.my_tags import encode_url
from post.form import OfferModelForm, ProblemModelForm
from post.models import ProblemModel, OfferModel, LikeOfferModel, LikeProblemModel, CommentOfferModel, \
    LikeCommentOfferModel, LikeCommentProblemModel, CommentProblemModel
from utils.hasher import decode_url


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def create_offer_view(request):
    if request.method == 'POST':
        form = OfferModelForm(request.POST)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.user = request.user
            offer.save()
            return redirect('common:home')
        else:
            context = {
                'form_data': request.POST,
                'errors': form.errors,
            }
            return render(request, 'forms/offer-form.html', context)
    return render(request, 'forms/offer-form.html')


def create_problem_view(request):
    if request.method == 'POST':
        form = ProblemModelForm(request.POST)
        anonym = request.POST.get('anonymous')
        if form.is_valid():
            problem = form.save(commit=False)
            if anonym is None:
                if request.user.is_authenticated:
                    problem.user = request.user
            problem.ip_address = get_client_ip(request)
            problem.save()
            return redirect('common:home')
        else:
            print(request.POST)
            context = {
                'form_data': request.POST,
                'errors': form.errors,
            }
            return render(request, 'forms/offer-form.html', context)
    return render(request, 'forms/offer-form.html')


def offers_problems_view(request):
    q = request.GET.get('q')
    offers = OfferModel.objects.all().order_by('-created_at')
    problems = ProblemModel.objects.all().order_by('-created_at')
    my_offers = []
    distinct_comments = []
    if request.user.is_authenticated:
        my_offers = OfferModel.objects.filter(user=request.user).order_by('-created_at')
        offers_comments = OfferModel.objects.filter(comments__user=request.user).order_by('-created_at')
        problems_comments = ProblemModel.objects.filter(comments__user=request.user).order_by('-created_at')

        my_comments = list(chain(offers_comments, problems_comments))

        seen_ids = set()
        distinct_comments = []

        for comment in my_comments:
            if comment.id not in seen_ids:
                seen_ids.add(comment.id)
                distinct_comments.append(comment)

        distinct_comments = sorted(distinct_comments, key=lambda x: x.created_at, reverse=True)

    if q:
        offers = offers.filter(title__icontains=q)
        problems = problems.filter(title__icontains=q)

    else:
        q = ''

    context = {
        'offers': offers,
        'problems': problems,
        'my_offers': my_offers,
        'my_comments': distinct_comments,
        'q': q,
    }
    return render(request, 'offers/offer.html', context)


def offer_detail_view(request, pk, url):
    redirect_url = decode_url(url)

    offer = get_object_or_404(OfferModel, pk=pk)
    offer.total_views += 1
    offer.save()

    comments = offer.comments.all().order_by('-created_at')
    commented_users = User.objects.filter(offer_comments__offer=offer).distinct()

    context = {
        'offer': offer,
        'comments': comments,
        'commented_users': commented_users,
        'redirect_url': redirect_url,
    }
    return render(request, 'comments/comment.html', context)

def problem_detail_view(request, pk, url):
    redirect_url = decode_url(url)
    problem = ProblemModel.objects.get(pk=pk)
    problem.total_views += 1
    problem.save()
    comments = problem.comments.all().order_by('-created_at')
    commented_users = User.objects.filter(problem_comments__problem=problem).distinct()

    context = {
        'offer': problem,
        'comments': comments,
        'commented_users': commented_users,
        'redirect_url': redirect_url,
    }
    return render(request, 'comments/comment.html', context)


def offer_comment_poster_view(request, pk):
    redirect_url = encode_url(request.POST.get('redirect_url'))
    if request.method == 'POST':
        content = request.POST.get('comment')
        if content:
            if request.user.is_authenticated:
                offer = OfferModel.objects.get(pk=pk)
                offer.comments.create(user=request.user, comment=content)
                return redirect('post:offer_detail', pk=pk, url=redirect_url)
            else:
                return redirect('auth:login')
    return redirect('post:offer_detail', pk=pk, url=redirect_url)


def problem_comment_poster_view(request, pk):
    redirect_url = encode_url(request.POST.get('redirect_url'))
    if request.method == 'POST':
        content = request.POST.get('comment')
        if content:
            if request.user.is_authenticated:
                problem = ProblemModel.objects.get(pk=pk)
                problem.comments.create(user=request.user, comment=content)
                return redirect('post:problem_detail', pk=pk, url=redirect_url)
            else:
                return redirect('auth:login')
    return redirect('post:problem_detail', pk=pk, url=redirect_url)


def like_offer_view(request, pk):
    before_path = request.POST.get('before')
    offer = OfferModel.objects.get(pk=pk)
    if LikeOfferModel.objects.filter(offer=offer):
        like = LikeOfferModel.objects.filter(offer=offer).first()
        if request.user in like.user.all():
            like.user.remove(request.user)
            return redirect(f'{before_path}')
        like.user.add(request.user)
        return redirect(f'{before_path}')
    like = LikeOfferModel.objects.create(
        offer=offer
    )
    like.user.add(request.user)
    return redirect(f'{before_path}')


def like_problem_view(request, pk):
    before_path = request.POST.get('before')
    problem = ProblemModel.objects.get(pk=pk)
    if LikeProblemModel.objects.filter(problem=problem):
        like = LikeProblemModel.objects.filter(problem=problem).first()
        if request.user in like.user.all():
            like.user.remove(request.user)
            return redirect(f'{before_path}')
        like.user.add(request.user)
        return redirect(f'{before_path}')
    like = LikeProblemModel.objects.create(
        problem=problem
    )
    like.user.add(request.user)
    return redirect(f'{before_path}')


def like_offer_comment_view(request, pk):
    before_path = request.POST.get('before')
    offer_comment = CommentOfferModel.objects.get(pk=pk)
    if LikeCommentOfferModel.objects.filter(offer_comment=offer_comment):
        like = LikeCommentOfferModel.objects.filter(offer_comment=offer_comment).first()
        if request.user in like.user.all():
            like.user.remove(request.user)
            return redirect(f'{before_path}')
        like.user.add(request.user)
        return redirect(f'{before_path}')
    like = LikeCommentOfferModel.objects.create(
        offer_comment=offer_comment
    )
    like.user.add(request.user)
    return redirect(f'{before_path}')


def like_problem_comment_view(request, pk):
    before_path = request.POST.get('before')
    problem_comment = CommentProblemModel.objects.get(pk=pk)
    if LikeCommentProblemModel.objects.filter(problem_comment=problem_comment):
        like = LikeCommentProblemModel.objects.filter(problem_comment=problem_comment).first()
        if request.user in like.user.all():
            like.user.remove(request.user)
            return redirect(f'{before_path}')
        like.user.add(request.user)
        return redirect(f'{before_path}')
    like = LikeCommentProblemModel.objects.create(
        problem_comment=problem_comment
    )
    like.user.add(request.user)
    return redirect(f'{before_path}')