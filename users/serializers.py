from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = (
            "id",
            "email",
            "is_teacher",
            "full_name",
        )
        read_only_fields = ("is_teacher",)
