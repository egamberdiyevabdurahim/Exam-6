from django.contrib import admin

from users.models import ProfileModel, TeamModel, UserModel
from post.admin import UsefulAdmin


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'is_active', 'created_at')
    list_display_links = list_display
    ordering = ('-created_at',)
    search_fields = ('id',
                     'email',
                     'first_name',
                     'last_name')
    list_filter = ('created_at', 'is_active')


@admin.register(ProfileModel)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user__email', 'organization_name', 'created_at')
    list_display_links = list_display
    ordering = ('-created_at',)
    search_fields = ('id',
                     'user__email',
                     'user__first_name',
                     'user__last_name',
                     'user__username',
                     'location',
                     'linkedin_link',
                     'organization_name')
    list_filter = ('created_at', 'user__email')


@admin.register(TeamModel)
class TeamModelAdmin(UsefulAdmin):
    list_display = ('id', 'first_name', 'last_name', 'profession', 'created_at')
    list_display_links = list_display
    ordering = ('-created_at',)
    search_fields = ('id',
                     'first_name',
                     'last_name',
                     'profession')
    list_filter = ('created_at', 'profession')
