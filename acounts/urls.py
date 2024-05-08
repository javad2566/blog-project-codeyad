from django.urls import path
from . import views

app_name = 'acount'
urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('signin/', views.signin_view, name="signin"),
    path('edit/', views.edit_profile, name="edit")
]
