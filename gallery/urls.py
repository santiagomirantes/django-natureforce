from django.urls import path, re_path
from gallery import views

urlpatterns = [
    path("",views.index, name="index"),
    path("gallery", views.gallery, name="gallery"),
    path("addPhoto",views.addPhoto, name="addPhoto"),
    path("addArtist", views.addArtist, name="addArtist"),
    path("search/",views.searchPicture,name="search"),
    path("singlePhoto/<photoURL>", views.singlePhoto, name="singlePhoto"),
    path("editPhoto/<photoURL>", views.editPhoto, name="editPhoto"),
    path("singlePhoto/deletePhoto/<photoURL>", views.deletePhoto, name="deletePhoto"),
    path("about",views.about,name="about")
]