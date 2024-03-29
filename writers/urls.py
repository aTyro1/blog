from django.urls import path
from . import views

urlpatterns=[
    path('',views.login,name='login'),
    path('validate',views.validate,name='validate'),
    path('register',views.register,name='register'),
    path('step1',views.step1,name='step1'),
    path('step2',views.success,name='step2'),
    path('otplogin',views.login_otp,name='login_otp'),
    path('afterLogin',views.login,name='login'),
    path('default',views.normal_login,name='normal login'),
    path('messagedLogin',views.messagedLogin,name='message based login')
]