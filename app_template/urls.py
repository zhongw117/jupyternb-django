from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('pipeline', views.pipeline, name='pipeline'),
    path('missingvalues', views.missingvalues, name='missingvalues'),
]