from django.urls import path 
from . import views
urlpatterns=[
    path('multiply/',view=views.multiply)
]