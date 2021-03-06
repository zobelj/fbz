"""fbz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from pages.views import home_view, about_view, school_view, school_view_update, schools_view, conference_view, update_database, calculate_view, logout_view, register_view

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('about/', about_view, name='about'),
    path('schools/', schools_view, name='schools'),
    path('schools/<str:school_name>/', school_view, name='school'),
    path('schools/<str:school_name>/true', school_view_update, name='school_update'),
    path('conference/<str:conference_name>/', conference_view, name='conference'),
    path('update_database/', update_database, name='update_database'),
    path('calculate/', calculate_view, name='calculate'),
    path('logout/', logout_view, name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', register_view, name='register'),
]
