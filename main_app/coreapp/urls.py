from django.urls import path
from . import views

urlpatterns = [
    path("", views.basicScrap, name='scrap')
]
