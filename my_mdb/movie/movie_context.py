from .models import Movie

def movies_slider(request):
    movies = Movie.objects.all().order_by('created_at')[:3]
    return {'slider_movies': movies}