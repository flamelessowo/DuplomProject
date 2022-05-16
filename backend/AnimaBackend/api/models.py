from django.db import models
from .helpers import PathAndRename

from AnimaBackend import settings

ANIME_TYPES = [
    ('TV', 'TV Series'),
    ('OVA', 'OVA'),
    ('FILM', 'FILM')
]

STATUS = [
    ('Airing', 'Airing'),
    ('Ended', 'Ended')
]

RATINGS = [
    (1, 'Insignificantly'),
    (2, 'Ugly'),
    (3, 'Bad'),
    (4, 'Anyhow'),
    (5, 'Mediocre'),
    (6, 'Not bad'),
    (7, 'Good'),
    (8, 'Great'),
    (9, 'Superb'),
    (10, 'Masterpiece')

]

MEDIA_IMG_PATH = 'images/'
MEDIA_VID_PATH = 'videos/'


class Genre(models.Model):
    title = models.CharField(verbose_name='Title', max_length=254, null=False)
    description = models.TextField(max_length=5000, null=False)
    slug = models.SlugField(default='dummy-slug', verbose_name='Slug')
    image = models.ImageField(default='f', upload_to=PathAndRename(MEDIA_IMG_PATH + 'genres'))

    def __str__(self) -> str:
        return self.title

    class Meta:
        managed = True
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
        ordering = ['-title']


class SubGenre(models.Model):
    genre_of = models.ManyToManyField(Genre, related_name='sub_genre')

    title = models.CharField(verbose_name='Title', max_length=254, null=False)
    description = models.TextField(max_length=5000, null=False)
    slug = models.SlugField(default='dummy-slug', verbose_name='Slug')
    image = models.ImageField(default='f', upload_to=PathAndRename(MEDIA_IMG_PATH + 'subgenres'))

    def __str__(self) -> str:
        return self.title

    class Meta:
        managed = True
        verbose_name = 'Sub Genre'
        verbose_name_plural = 'Sub Genres'
        ordering = ['-title']


class Studio(models.Model):
    name = models.CharField(max_length=254, unique=True, null=False)

    class Meta:
        managed = True
        verbose_name = 'Studio'
        verbose_name_plural = 'Studios'
        ordering = ['-name']

    def __str__(self) -> str:
        return self.name


class Anime(models.Model):
    title = models.CharField(verbose_name='Title', max_length=254, null=False)
    description = models.TextField(verbose_name='Description', max_length=5000, null=False)
    categories = models.ManyToManyField(Genre, verbose_name='Categories')
    series = models.PositiveIntegerField(verbose_name='Series', null=False, default=0)
    type = models.CharField(choices=ANIME_TYPES, null=False, max_length=30)
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE)
    date_aired = models.DateTimeField(verbose_name='Airing started')
    date_aired_end = models.DateTimeField(verbose_name='Airing ended')
    status = models.CharField(choices=STATUS, null=False, verbose_name='Status', max_length=50)
    rating = models.IntegerField(choices=RATINGS, null=False)
    views = models.PositiveIntegerField(default=0)
    trending = models.BooleanField(default=False)
    popular = models.BooleanField(default=False)
    image = models.ImageField(verbose_name="Image", upload_to=PathAndRename(MEDIA_IMG_PATH + 'animes'), default='f')
    slug = models.SlugField(verbose_name='Slug', default='dummy-anime')

    @property
    def get_absolute_image_url(self):
        return "{0}{1}".format(settings.MEDIA_URL, self.image.url)

    @property
    def get_str_genres(self):
        return ''.join(str(genre) + ', ' for genre in self.categories.all())[:-2]

    def __str__(self) -> str:
        return self.title

    class Meta:
        managed = True
        verbose_name = 'Anime'
        verbose_name_plural = 'Animes'
        ordering = ['title', '-rating']


class Banner(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, null=False)
    description = models.TextField(blank=True)
    banner_image = models.ImageField(verbose_name='Banner Image', null=False,
                                     upload_to=PathAndRename(MEDIA_IMG_PATH + 'banners'))

    def __str__(self) -> str:
        return self.anime.title + ' Banner'
