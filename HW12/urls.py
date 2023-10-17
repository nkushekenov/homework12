from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get_columns/', views.get_specific_columns, name='get_columns'),
    path('exclude_values/', views.exclude_specific_values, name='exclude_values'),
]
