from rest_framework import serializers
from .models import Theater


class TheaterSerializer(serializers.ModelSerializer):
    number = serializers.IntegerField(required=False, default=0)

    class Meta:
        model = Theater
        fields = "__all__"

    def validate_number(self, value):
        if Theater.objects.filter(number=value).exists():
            raise serializers.ValidationError({"error": "theater_already_exists"})
