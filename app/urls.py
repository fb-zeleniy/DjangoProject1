from django.contrib import admin
from django.urls import path,include
from .views import *

app_name="app"
urlpatterns = [
    path('all/',index,name='all'),
    path('python/',index2,name='index2'),
    path('html/',index_html,name='index_html'),
    path('rubric/<int:pk>/',detail,name='detail'),
    path('bb/<int:pk>/', detail_bb, name='detail_bb'),
    path('home/', home, name='home'),
    path('about/', about, name='home'),
    path('contacts/', contacts, name='home'),
]

# app_name = "to_do_list"
# urlpatterns[
#     path('', views.task_list, name='task_list'),
#     path('add/', (views.task_create, name='task_add'),
#     path('edit/<int:pk>/', views.task_edit, name='task_edit'),
#     path('delete/<int:pk>/', views.task_delete, name='task_delete'),
#     path('complete/<int:pk>/', views.task_complete, name='task_complete'),
# ]