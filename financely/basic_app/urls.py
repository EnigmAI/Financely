from django.urls import path
from basic_app import views

app_name = 'basic_app'
urlpatterns = [
    path('', views.dashboard,name="dashboard"),
    path('home/', views.index, name='index'),
    path('profile/',views.profile, name ='profile'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('home/<str:symbol>', views.stock, name = "stock"),
    path('login/', views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('register/',views.registerPage,name="register"),


]
