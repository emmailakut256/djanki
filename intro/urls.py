from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path("intro/", views.intro, name="intro"),
    path("intro/members", views.members, name="members"),
    path("intro/details/<slug:slug>", views.details, name="details"),
    path("intro/testing/", views.testing, name='testing'),
]
