from django.urls import path
from django.views.generic.base import TemplateView
from forms.views import data

urlpatterns = [
    path('', data)#.index, name='index'),
]
