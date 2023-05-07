from django.urls import path

from crud_app import views

app_name = 'crud_app'

urlpatterns = [
    # C
    path('create/', views.task_create_view, name='task_create_view'),
    # R
    path('list/', views.task_list_view, name='task_list_view'),
    path('<int:pk>/', views.task_detail_view, name='task_detail_view'),
    # U
    path('update/<int:pk>/', views.task_update_view, name='task_update_view')
]
