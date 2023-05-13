from django.urls import path
from . import views

urlpatterns = [
    path("przemek", views.przemek, name="przemek"),
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet")

]