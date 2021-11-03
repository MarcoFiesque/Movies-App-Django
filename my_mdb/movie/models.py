from django.db import models
from django.utils.text import slugify

CATEGORY_CHOICES = (
    ('action', 'ACTION'),
    ('comedy', 'COMEDY'),
    ('drama', 'DRAMA'),
    ('fantasy', 'FANTASY'),
    ('horror', 'HORROR'),
    ('kids', 'KIDS'),
    ('romance', 'ROMANCE'),
    ('science-fiction', 'SCIENCE-FICTION'),
)

LANGUAGE_CHOICES = (
    ('english', 'ENGLISH'),
    ('french', 'FRENCH'),
)

STATUS_CHOICES = (
    ('RA', 'RECENTLY ADDED'),
    ('MW', 'MOST WATCHED'),
    ('TR', 'TOP RATED'),
)

class Movie(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='movies')
    banner = models.ImageField(upload_to='movies_banner')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=15)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=8)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)
    cast = models.CharField(max_length=100)
    year_of_production = models.DateField()
    views_count = models.IntegerField(default=0)
    slug = models.SlugField(blank=True, null=True)
    trailer = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, force_insert: bool = True, force_update: bool = True, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Movie, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title

LINK_CHOICES = (
    ('Download', 'DOWNLOAD LINK'),
    ('Watch', 'WATCH LINK'),
)

class Movielink(models.Model):
    movie = models.ForeignKey(Movie, related_name='movie_watch_link', on_delete=models.CASCADE)
    type = models.CharField(choices=LINK_CHOICES, max_length=8)
    link = models.URLField()

    def __str__(self):
        string = str(self.movie) + ' | ' + str(self.type)
        return string

