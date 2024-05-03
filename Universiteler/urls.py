from django.urls import path
from . import views

urlpatterns = [
    path("", views.universiteler, name="universiteler"),
]