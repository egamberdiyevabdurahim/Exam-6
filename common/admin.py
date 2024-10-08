from django.contrib import admin

from common.models import AboutModel, QuestionModel
from post.admin import UsefulAdmin


@admin.register(AboutModel)
class AboutModelAdmin(UsefulAdmin):
    list_display = ('id', 'title', 'created_at')
    list_display_links = list_display
    ordering = ('-created_at',)
    search_fields = ('id', 'title', 'description')
    list_filter = ('created_at',)


@admin.register(QuestionModel)
class QuestionModelAdmin(UsefulAdmin):
    list_display = ('id', 'question', 'created_at')
    list_display_links = list_display
    ordering = ('-created_at',)
    search_fields = ('id', 'question', 'answer')
    list_filter = ('created_at',)
