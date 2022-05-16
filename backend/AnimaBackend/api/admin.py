from django.contrib import admin

from .models import Anime, Banner, Genre, SubGenre, Studio

admin.site.register(Anime)
admin.site.register(Banner)
admin.site.register(Genre)
admin.site.register(SubGenre)
admin.site.register(Studio)
