from django.urls import path

from next_app import views


urlpatterns = [
    path('hello/', views.hello),
    path('hello/eva', views.eva),

    path('hello/<str:data>', views.name),

    path('hello2/', views.hello2),
    path('hello2/<str:data>', views.name2),
]
