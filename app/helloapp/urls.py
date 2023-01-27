from django.urls import path
from helloapp import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]