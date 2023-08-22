from django.urls import path
from gallery import views

urlpatterns = [
    path("",views.index, name="index"),
    path("gallery", views.gallery, name="gallery"),
    path("addPhoto",views.addPhoto, name="addPhoto"),
    path("addArtist", views.addArtist, name="addArtist"),
    path("search/",views.searchPicture,name="search"),
    path("account",views.account,name="account"),
    path("register",views.register,name="register"),
    path("login", views.login, name="login")
]