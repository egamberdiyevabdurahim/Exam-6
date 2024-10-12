from django.db import models
from django.utils.translation import gettext_lazy as _


class UsefulModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AboutModel(UsefulModel):
    title = models.CharField(max_length=128, verbose_name=_('About Title'))
    description = models.TextField(verbose_name=_('About Description'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("About Us")
        verbose_name_plural = _("About Us")


class QuestionModel(UsefulModel):
    question = models.CharField(max_length=128, verbose_name=_('Question'))
    answer = models.TextField(verbose_name=_('Answer'))

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
