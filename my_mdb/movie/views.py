from django.db.models.query import QuerySet
from django.http.response import HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, YearArchiveView
from django.views.generic.dates import YearArchiveView
from .models import Movie, Movielink

# def index(request):
#     if request.method == 'GET':
#         return render(request, 'movie/index.html')
#     else:
#         return HttpResponseBadRequest('Bad request')

class HomeView(ListView):
    model = Movie
    template_name = 'movie/index.html'
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['top_rated'] = Movie.objects.filter(status='TR')
        context['most_watched'] = Movie.objects.filter(status='MW')
        context['recently_added'] = Movie.objects.filter(status='RA')
        print(context)
        return context

class MovieList(ListView):
    model = Movie
    template_name='movie/movie_list.html'
    paginate_by = 2

class MovieDetail(DetailView):
    model = Movie
    template_name='movie/movie_detail.html'
    
    def get_object(self):
        object = super(MovieDetail, self).get_object()
        # object.views_count += 1
        # object.save()
        return object

    def get_context_data(self, **kwargs):
        context = super(MovieDetail, self).get_context_data(**kwargs)
        context['links'] = Movielink.objects.filter(movie=self.get_object())
        context['related_movies'] = Movie.objects.filter(category=self.get_object().category).exclude(id=self.get_object().id).order_by('created_at')[:6]
        print(context['related_movies'])
        return context

class MovieCategory(ListView):
    model = Movie
    paginate_by = 2
    def get_queryset(self):
        self.category = self.kwargs['category']
        movies = Movie.objects.filter(category=self.category)
        print(self.category)
        return movies
        # return Movie.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(MovieCategory, self).get_context_data(**kwargs)
        context['movie_category'] = self.category
        return context
        
class MovieLanguage(ListView):
    model = Movie
    paginate_by = 2

    def get_queryset(self):
        self.language = self.kwargs['lang']
        movies = Movie.objects.filter(language=self.language)
        print(self.language)
        return movies
        # return Movie.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(MovieLanguage, self).get_context_data(**kwargs)
        context['movie_language'] = self.language
        return context

class MovieSearch(ListView):
    model = Movie
    paginate_by = 2

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            object_list = Movie.objects.filter(title__icontains=query)
        else:
            object_list = Movie.objects.all()
        return object_list

    # def get_context_data(self, **kwargs):
    #     context = super(MovieLanguage, self).get_context_data(**kwargs)
    #     context['movie_language'] = self.language
    #     return context

class MovieYear(YearArchiveView):
    movies = Movie.objects.all()
    date_field = 'year_of_production'
    make_object_list = True
    allow_future = True
    
    template_name = 'movie/movie_list.html'

    def get_allow_empty(self) -> bool:
        return True

    def get_queryset(self):
        return self.movies

