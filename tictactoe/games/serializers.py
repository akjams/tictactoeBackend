from .models import User, Game
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"
