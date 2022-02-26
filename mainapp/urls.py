from django.urls import path, include

# import mainapp
from mainapp.views import main
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', main, name='main'),
]