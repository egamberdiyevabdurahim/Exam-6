import base64

from django import template


register = template.Library()


@register.simple_tag
def get_full_url(request, lang):
    url = request.path.split('/')
    url[1] = lang
    return '/'.join(url)


@register.simple_tag
def get_url(request):
    full_url = request.build_absolute_uri()
    return full_url


@register.simple_tag
def get_current_lang(request):
    return request.LANGUAGE_CODE[:2]


@register.simple_tag
def get_offer_or_problem(request):
    url = request.path.split('/')
    if url[3] == 'create_problem':
        return 'Problem'

    elif url[3] == 'create_offer':
        return 'Offer'


@register.simple_tag
def get_offer_or_problem_detail(request):
    url = request.path.split('/')
    print(url)
    if url[3] == 'problem_detail':
        return 'Problem'

    elif url[3] == 'offer_detail':
        return 'Offer'


@register.simple_tag
def encode_url(url):
    return base64.urlsafe_b64encode(url.encode('utf-8')).decode('utf-8').rstrip('=')