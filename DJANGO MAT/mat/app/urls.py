from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('main/',views.mainpage,name='mainpage'),
    path("login/",views.login_user,name='login'),
    path("signup/",views.signup,name='signup'),
    path('logout/',views.logout_user,name='logout'),
    path('delete/<uid>',views.delete,name='delete'),
]
