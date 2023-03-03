from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('main', views.homepage),
    path('User/login', views.login),
    path('EnthusiastReg', views.EnthusiastFormReg),
    path('AlphaPremiumReg', views.AlphaPremiumFormReg),
    path('BetaPremiumReg', views.BetaPremiumFormReg),
    path('User/<str:Name>-B<str:Id>aA', views.UserPage),
    path('login', views.login),
]
