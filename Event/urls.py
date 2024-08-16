from django.urls import path
from Event import views

urlpatterns = [
    path('',views.Home.as_view(), name= 'home'),
]
