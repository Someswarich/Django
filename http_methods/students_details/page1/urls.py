from django.urls import path
from . import views
urlpatterns=[
    path("stu_data/",view=views.details)
    # path("stu_data/",view=views.checking_exist_or_not)
]