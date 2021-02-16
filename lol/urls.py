from django.urls import path

from . import views

app_name = "lol"

urlpatterns = [
    path("summoner/", views.SearchMatchView.as_view(), name="summoner"),
]
