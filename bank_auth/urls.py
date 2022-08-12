from django.urls import path

from .views import CreateProfileView, HomeView, LoginView, LogoutView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("create_profile/", CreateProfileView.as_view(), name="create_profile"),

]
