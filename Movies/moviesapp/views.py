from django.http import HttpResponse
from models import Movie
from django.template import Context, loader
#from django.shortcuts import render_to_response


def home(request):
    movie_list = Movie.objects.all().order_by('title')[:5]
    template = loader.get_template('home.html')
    context = Context({
        'movies' : movie_list,})
    return HttpResponse(template.render(context))
    

# def linkhandler(request):
#     context = Context()
#     return render_to_response()
