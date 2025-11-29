from django.urls import path
from . import views
urlpatterns=[
    path("",view=views.get,name='get'),
    path("add/",view=views.add ,name='add'),
    path("update/<int:user_id>/",view=views.update,name='update'),
     path("delete/<int:user_id>/",view=views.delete,name='delete')
]
