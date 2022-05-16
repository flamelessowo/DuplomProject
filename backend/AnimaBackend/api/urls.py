from django.urls import path
from .views import IndexView, detail_anime_view, GenreView

urlpatterns = [
    path('animes/', IndexView.as_view()),
    path('genres/', GenreView.as_view()),
    path('anime/<slug>', detail_anime_view)
]