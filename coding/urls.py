from django.urls import path
from . import views

app_name = 'coding'
urlpatterns = [
    path('', views.get_code, name='get_code',),
]
