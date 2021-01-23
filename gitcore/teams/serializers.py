from rest_framework.serializers import ModelSerializer
from .models import Team, TeamGroup


class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class TeamGroupSerializer(ModelSerializer):
    class Meta:
        model = TeamGroup
        fields = "__all__"
