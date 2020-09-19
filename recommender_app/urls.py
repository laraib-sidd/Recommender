from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("anime/", views.anime, name="anime"),
    path("anime/results/", views.anime_results, name="anime_results"),
    path("music/", views.music, name="music"),
    path("signup/", views.signup, name="signup"),
]
