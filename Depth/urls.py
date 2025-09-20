from django.contrib import admin
from django.urls import path
from Depth_company import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sign_up", views.sign_up, name="sign_up")
]