from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils.translation import gettext_lazy as _  # Correct translation import
from common.models import UsefulModel


class ProfileModel(UsefulModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("Profile"), related_name='profile')
    organization_name = models.CharField(verbose_name=_("Organization Name"), max_length=64, null=True, blank=True)
    location = models.CharField(verbose_name=_("Location"), max_length=64, null=True, blank=True)
    linkedin_link = models.CharField(verbose_name=_("Linkedin"), max_length=64, null=True, blank=True)
    avatar = models.ImageField(verbose_name=_("Avatar"), upload_to="users/", default='default.jpg')

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")


class TeamModel(UsefulModel):
    first_name = models.CharField(verbose_name=_("First Name"), max_length=64)
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=64)
    profession = models.CharField(verbose_name=_("Profession"), max_length=128)
    avatar = models.ImageField(verbose_name=_("Avatar"), upload_to="team/", default='default.jpg')
    description = models.TextField(verbose_name=_("Description"), null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _("Team Member")
        verbose_name_plural = _("Team Members")

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"