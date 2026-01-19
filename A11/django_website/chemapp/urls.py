from django.urls import path

from . import views

app_name = 'chemapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('chembl/', views.chembl, name='chembl'),
    path('povray/', views.povray, name='povray')
]