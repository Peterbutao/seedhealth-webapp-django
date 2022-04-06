from django.urls import path
from plantdiseases import views


urlpatterns = [
    path('', views.app)
]