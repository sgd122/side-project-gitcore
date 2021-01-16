from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LOGIN_EMAIL = "email"
    LOGIN_GITHUB = "github"
    LOGIN_KAKAO = "kakao"

    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGIN_GITHUB, "Github"),
        (LOGIN_KAKAO, "Kakao"),
    )

    avatar = models.ImageField(upload_to="avatars", blank=True, verbose_name="프로필사진")
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, blank=True, verbose_name="성별"
    )
    login_method = models.CharField(
        max_length=50, choices=LOGIN_CHOICES, default=LOGIN_GITHUB, verbose_name="로그인 수단"
    )

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})
