from modeltranslation.translator import TranslationOptions, register

from common.models import AboutModel, QuestionModel


@register(AboutModel)
class AboutModelTranslation(TranslationOptions):
    fields = ('title', 'description')


@register(QuestionModel)
class QuestionModelTranslation(TranslationOptions):
    fields = ('question', 'answer')
