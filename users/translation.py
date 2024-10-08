from modeltranslation.translator import TranslationOptions, register

from users.models import TeamModel


@register(TeamModel)
class TeamModelTranslation(TranslationOptions):
    fields = ('profession', 'description')
