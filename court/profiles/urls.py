from django.urls import path, include
from . import views
# SET THE NAMESPACE!
# Be careful setting the name to just /login use userlogin instead!
appname = 'profiles'
urlpatterns=[
    path('index/', views.dashboard, name='index'),
    path('Dashboard/', views.Dashboard_view, name='Dashboard'),
    path('', views.dashboard, name='index'),
    path('register/',views.register_view,name='register'),
    path('user_login/',views.user_login,name='loginpage'),
    path("logout", views.logout_request, name="logout"),

]                                                             
