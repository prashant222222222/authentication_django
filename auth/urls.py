from django.urls import path

from auth import views
urlpatterns = [
    # path('login/', views.auth_login),
    path('login/', views.Login.as_view()),
    path('logout/', views.Logout.as_view()),
]
