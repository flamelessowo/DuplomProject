from rest_framework import serializers
from .models import Anime, Genre, SubGenre


class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    sub_genres = serializers.SerializerMethodField('get_subgenres')

    class Meta:
        model = Genre
        fields = '__all__'

    def get_subgenres(self, item):
        sub_genres = SubGenre.objects.filter(genre_of=item)
        if not sub_genres:
            return None
        sub_genres = sub_genres.values_list('id', flat=True)
        return sub_genres


class SubGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubGenre
        fields = '__all__'
        exclude = ['genre_of']


