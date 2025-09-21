from django.contrib import admin
from django.urls import path
from Depth_company import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sign_up", views.sign_up, name="sign_up"),
    path("login_page", views.login_page, name="login_page"),
    path("about_us", views.about_us, name="about_us")
]