from django.conf.urls import include,url
from . import views
app_name = 'movie'
urlpatterns = [
    url(r'', views.movie_list, name="movie"),
]
