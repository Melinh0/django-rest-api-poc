from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

    def validate(self, attrs):
        if Movie.objects.filter(
            name=attrs["name"],
            director=attrs["director"],
            duration=attrs["duration"],
        ).exists():
            raise serializers.ValidationError({"error": "movie_already_exists"})
        return attrs
