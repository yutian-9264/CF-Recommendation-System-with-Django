"""MovieRec URL Configuration

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
from django.urls import path,re_path

import App
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', App.views.WelcomePage, name='Home'),
    path('Welcome', App.views.WelcomePage),

    path('Index',App.views.IndexPage, name='Index'),
    path('Registration',App.views.Userreg, name='Reg'),
    path('Login',App.views.loginpage,name='Loginpage'),
    path('Logout', App.views.logout, name='Logout'),
    path('Rate', App.views.show_view,name='Rate'),
    path('detail', App.views.detail, name='Detail'),
    path('Review',App.views.review,name='Review'),
    path('Recommendation',App.views.recommend,name='Recommendation'),
    path('GetRec',App.views.get_rec,name='GetRec'),
    path('test',App.views.testPage, name='Test'),

    re_path('(\d+)/',App.views.detail)


]
