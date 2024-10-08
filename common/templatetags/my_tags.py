from django import template


register = template.Library()


@register.simple_tag
def get_full_url(request, lang):
    url = request.path.split('/')
    url[1] = lang[0]
    return '/'.join(url)


@register.simple_tag
def get_current_lang(request):
    return request.LANGUAGE_CODE[:2]