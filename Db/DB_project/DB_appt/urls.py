from django.urls import path
from . import views
urlpatterns=[
    path("Employee/",view=views.employee),
    path("Student/",view=views.student_data)
]