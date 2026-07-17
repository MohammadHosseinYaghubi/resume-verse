from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def save(self):
        refresh = self.validated_data["refresh"]

        token = RefreshToken(refresh)

        token.blacklist()