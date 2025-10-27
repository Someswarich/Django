from django.urls import path
from . import views
urlpatterns=[
    path("get_user/",view=views.get_user),
    path("reg_user/",view=views.reg_user),
    path("update_user/<int:id>/",view=views.update_user)
]