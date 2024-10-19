from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from common.models import UsefulModel


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('Users must have an email address'))

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)


class UserModel(AbstractBaseUser, PermissionsMixin, UsefulModel):
    email = models.EmailField(verbose_name=_("Email Address"), unique=True)
    first_name = models.CharField(verbose_name=_("First Name"), max_length=64)
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=64, null=True, blank=True)
    is_staff = models.BooleanField(verbose_name=_("Staff Status"), default=False)
    is_active = models.BooleanField(verbose_name=_("Active"), default=True)
    date_joined = models.DateTimeField(verbose_name=_("Date Joined"), auto_now_add=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'first_name']

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")


class ProfileModel(UsefulModel):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, verbose_name=_("Profile"), related_name='profile')
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
    avatar = models.ImageField(verbose_name=_("Avatar"), upload_to="team/", default='assets/my/default.jpg')
    description = models.TextField(verbose_name=_("Description"), null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _("Team Member")
        verbose_name_plural = _("Team Members")

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"