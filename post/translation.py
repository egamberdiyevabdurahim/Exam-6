from modeltranslation.translator import TranslationOptions, register

from post.models import ProblemModel, OfferModel


@register(ProblemModel)
class ProblemModelTranslation(TranslationOptions):
    fields = ('title', 'description')


@register(OfferModel)
class OfferModelTranslation(TranslationOptions):
    fields = ('title', 'description')
