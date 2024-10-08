from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from post.models import (ProblemModel, OfferModel, CommentOfferModel, CommentProblemModel,
                         LikeOfferModel, LikeProblemModel, LikeCommentOfferModel, LikeCommentProblemModel)


class UsefulAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(ProblemModel)
class ProblemModelAdmin(UsefulAdmin):
    list_display = ('id', 'title', 'user__username', 'created_at')
    list_display_links = list_display
    ordering = ('-created_at',)
    search_fields = ('id',
                     'title',
                     'user__username',
                     'user__email',
                     'user__first_name',
                     'user__last_name')
    list_filter = ('created_at', 'user__email')


@admin.register(OfferModel)
class OfferModelAdmin(UsefulAdmin):
    list_display = ('id', 'title', 'user__username', 'created_at')
    list_display_links = list_display
    ordering = ('-created_at',)
    search_fields = ('id',
                     'title',
                     'user__username',
                     'user__email',
                     'user__first_name',
                     'user__last_name')
    list_filter = ('created_at', 'user__email')


@admin.register(CommentOfferModel)
class CommentOfferModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'offer__title', 'user__username', 'created_at')
    list_display_links = list_display
    ordering = ('-created_at',)
    search_fields = ('id',
                     'offer__title',
                     'offer__description',
                     'user__username',
                     'user__email',
                     'user__first_name',
                     'user__last_name')
    list_filter = ('created_at', 'user__email')


@admin.register(CommentProblemModel)
class CommentProblemModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'problem__title', 'user__username', 'created_at')
    list_display_links = list_display
    ordering = ('-created_at',)
    search_fields = ('id',
                     'problem__title',
                     'problem__description',
                     'user__username',
                     'user__email',
                     'user__first_name',
                     'user__last_name')
    list_filter = ('created_at', 'user__email')


@admin.register(LikeOfferModel)
class LikeOfferModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'offer__title', 'user__username', 'created_at')
    list_display_links = list_display
    ordering = ('-created_at',)
    search_fields = ('id',
                     'offer__title',
                     'user__username',
                     'user__email',
                     'user__first_name',
                     'user__last_name')
    list_filter = ('created_at', 'user__email')


@admin.register(LikeProblemModel)
class LikeProblemModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'problem__title', 'user__username', 'created_at')
    list_display_links = list_display
    ordering = ('-created_at',)
    search_fields = ('id',
                     'problem__title',
                     'user__username',
                     'user__email',
                     'user__first_name',
                     'user__last_name')
    list_filter = ('created_at', 'user__email')


@admin.register(LikeCommentOfferModel)
class LikeCommentOfferModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user__username', 'created_at')
    list_display_links = list_display
    ordering = ('-created_at',)
    search_fields = ('id',
                     'user__username',
                     'user__email',
                     'user__first_name',
                     'user__last_name')
    list_filter = ('created_at', 'user__email')


@admin.register(LikeCommentProblemModel)
class LikeCommentProblemModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user__username', 'created_at')
    list_display_links = list_display
    ordering = ('-created_at',)
    search_fields = ('id',
                     'user__username',
                     'user__email',
                     'user__first_name',
                     'user__last_name')
    list_filter = ('created_at', 'user__email')