from django.contrib import admin
from .models import Team, TeamGroup


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('team', 'user')


@admin.register(TeamGroup)
class TeamGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'team_link')
