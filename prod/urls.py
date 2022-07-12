from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('save',views.save,name="save"),
    path('table',views.table,name="table"),
    path('edit/<str:pk>',views.edit,name="edit"),
]