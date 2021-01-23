from django.db import models
from django.utils.translation import ugettext_lazy as _


class TeamGroup(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("팀명"))
    description = models.TextField()
    team_link = models.CharField(max_length=10, verbose_name=_("링크"))

    def __str__(self):
        return self.name


class Team(models.Model):
    """ Team Model """

    team = models.ForeignKey(
        "TeamGroup", related_name="teams", on_delete=models.CASCADE, verbose_name=_("team")
    )
    user = models.ForeignKey(
        "users.User", related_name="teams", on_delete=models.CASCADE, verbose_name=_("팀원")
    )
