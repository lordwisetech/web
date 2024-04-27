from . import views
from .views import showtodo
from django.urls import path

urlpatterns = [

   path('',showtodo.as_view(),name="home"),
   path('create/',views.create,name="create"),
   path('delete/<int:pk>',views.delete,name="delete"),
   path('edit/<int:pk>', views.edit, name="edit")

]
