from django.urls import path
from . import views
urlpatterns=[
    path('get/',view=views.get),
    path('post_student/',view=views.post_student)

]