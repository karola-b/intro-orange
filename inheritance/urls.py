from django.urls import path

from inheritance import views

app_name = 'inheritance'

urlpatterns = [
    path('first/', views.first, name='first_name'),
    path('second/', views.first, name='second_name')
]
