from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Team, TeamGroup
from .serializers import TeamSerializer, TeamGroupSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamGroupViewSet(viewsets.ModelViewSet):
    queryset = TeamGroup.objects.all()
    serializer_class = TeamGroupSerializer
