from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, _("Male")),
        (GENDER_FEMALE, _("Female")),
        (GENDER_OTHER, _("Other")),
    )

    LOGIN_EMAIL = "email"
    LOGIN_GITHUB = "github"
    LOGIN_KAKAO = "kakao"

    LOGIN_CHOICES = (
        (LOGIN_EMAIL, _("Email")),
        (LOGIN_GITHUB, _("Github")),
        (LOGIN_KAKAO, _("Kakao")),
    )

    avatar = models.ImageField(upload_to="avatars", blank=True, verbose_name=_("프로필사진"))
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, blank=True, verbose_name=_("성별")
    )
    login_method = models.CharField(
        max_length=50, choices=LOGIN_CHOICES, default=LOGIN_GITHUB, verbose_name=_("로그인 수단")
    )

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})
