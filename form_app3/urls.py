from django.urls import path

from form_app3 import views

app_name = 'form_app3'

urlpatterns = [
    path('create/', views.task_create_view, name='task_create_view'),
    path('list/', views.task_list_view, name='task_list_view')
]
