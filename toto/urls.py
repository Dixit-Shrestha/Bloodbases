from django.contrib import admin
from django.urls import path, include 
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('index.html', views.index, name='index'),
    path('', views.index, name='index'),
    path('signin.html', views.user_signin,name='signin'),
    path('main.html', views.main,name='main'),
    path('service.html', views.service, name='service'),
    path('register.html', views.donor_req, name='register'),
    path('contact.html', views.contact, name='contact'),
    path('index.html', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('order.html', views.receipent_req, name='order'),
    path('login.html', views.user_login, name='login'),
    path('list.html', views.matched_donors, name='list'),
    path('forgot-password/', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset.html'
    ), name='forgot_password'),

    path('forgot-password/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'
    ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html'
    ), name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'
    ), name='password_reset_complete'),
 
]
