from django.urls import path
from accounts import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.account, name="account"),
    path("register",views.registerView, name="register"),
    path("login", views.loginView, name="login"),
    path("logout",LogoutView.as_view(template_name="logout/logout.html"), name = "logout"),
    path("editProfile",views.editProfile,name="editProfile")
]