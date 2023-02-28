from django.urls import path
from modvis_scraper import views

urlpatterns = [
    path('modvis_scraper', views.modvis_scraper, name='modvis_scraper'),
]