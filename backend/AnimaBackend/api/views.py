from rest_framework.response import Response
from rest_framework import generics, decorators, status
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from .models import Anime, Genre
from .serializers import AnimeSerializer, GenreSerializer


class IndexView(generics.ListAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer


class GenreView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


@decorators.api_view(['GET'])
def detail_anime_view(request, slug):
    if request.method == 'GET':
        try:
            anime = Anime.objects.get(slug=slug)
            serialized_anime = AnimeSerializer(anime)
            return Response(serialized_anime.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
