from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from gallery.models import *
from gallery.forms import *
from urllib.parse import unquote
from django.contrib.auth.decorators import login_required

def index(request) :


    dict = {
    }

    #rendering it

    return render(request, "index/index.html", dict)

@login_required
def gallery(request) :
    pictures = Photo.objects.all()

    #making a valid string to put the file path in the url (because it can´t include /)
    for picture in pictures:
      url = picture.file.url
      linkUrl = url.replace("/","%line%")
      picture.linkUrl = linkUrl
    return render(request, "gallery/gallery.html", {"pictures":pictures})

@login_required
def addPhoto(request):

    #creating the errors block

    errors = {
       "validArtist":True,
       "validYear":True,
       "validPhoto":True
    }

     #checking if the request method is post
    if request.method == "POST":

     #recieving the form

     form = AddPhotoForm(request.POST, request.FILES)

     #cheking all the possible artists and photos

     artists = Artist.objects.all()
     photos = Photo.objects.all()

     #creating a filter function

     def artistExists(name) :
       response = False
       for model in artists:
          if model.name == name :
             response = True

       return response
     
     def photoExists(name) :
       response = False
       for model in photos:
          if model.name == name :
             response = True

       return response
             

     #if the info is valid, recieves it.

     if form.is_valid():
         info = form.cleaned_data

         #checking if artist exists and year is valid

         if artistExists(info["artista"]) and not photoExists(info["nombre"]) and info["año"] > 1700 and info["año"] < 2023 :
          photo = Photo(name = info["nombre"], year = info["año"], file = info["archivo"], artist = info["artista"], description = info["descripcion"])
          photo.save()
          form = AddPhotoForm(None)
          return render(request, "addPhoto/addPhoto.html", {"form":form, "errors":errors})
         
         elif not photoExists(info["nombre"]) and info["año"] > 1700 and info["año"] < 2023:
          errors["validArtist"] = False
          return render(request, "addPhoto/addPhoto.html", {"form":form, "errors":errors})
         
         elif info["año"] > 1700 and info["año"] < 2023:
          errors["validPhoto"] = False
          return render(request, "addPhoto/addPhoto.html", {"form":form, "errors":errors})
         
         else:
          errors["validYear"] = False
          return render(request, "addPhoto/addPhoto.html", {"form":form, "errors":errors})
    
    else:
       form = AddPhotoForm()
    
    return render(request,"addPhoto/addPhoto.html", {"form":form, "errors":errors})

@login_required
def addArtist(request):
   
   #creating the error block

   errors = {
      "validAge":True
   }
   
   #checking if the request method is POST

   if request.method == "POST":
      
      #recieving the form

      form = AddArtistForm(request.POST)

      #if the info is valid, recieves it

      if form.is_valid():
         info = form.cleaned_data

         #checking age
         if info["edad"] > 5 and info["edad"] < 120:
            artist = Artist(name = info["nombre"], age = info["edad"], email = info["email"])
            artist.save()
            form = AddArtistForm(None)
            return render(request, "addArtist/addArtist.html", {"form":form, "errors":errors})
         else:
            form = AddArtistForm()
            errors["validAge"] = False

            return render(request, "addArtist/addArtist.html", {"form":form, "errors":errors})
   else:
         form = AddArtistForm()

   return render(request, "addArtist/addArtist.html", {"form":form, "errors":errors}) 

@login_required
def searchPicture(request) :

   search = request.GET["search"]
   pictures = []
   byName = Photo.objects.filter(name__icontains=search)
   byArtist = Photo.objects.filter(artist__icontains=search)

   pictures.extend(byName) 
   pictures.extend(byArtist)

   pictures = list(set(pictures))

    #making a valid string to put the file path in the url (because it can´t include /)
   for picture in pictures:
      url = picture.file.url
      linkUrl = url.replace("/","%line%")
      picture.linkUrl = linkUrl
   return render(request, "gallery/gallery.html", {"pictures":pictures})

@login_required
def singlePhoto(request, photoURL) :

   originalURL = unquote(photoURL)

   #getting the real photo URL replacing "%line%" with "/"
   photoURL = unquote(photoURL.replace("%line%", "/"))
   pictures = Photo.objects.all()
   picture = None

   for pic in pictures:
      if(pic.file.url == photoURL) :
         picture = pic

   
   return render(request, "singlePhoto/singlePhoto.html", {"photoURL":originalURL,"picture":picture,"delete":False})

@login_required
def editPhoto(request, photoURL):

   #getting the real photo URL replacing "%line%" with "/"
   photoURL = unquote(photoURL.replace("%line%", "/"))
   pictures = Photo.objects.all()
   photo = None

   for pic in pictures:
      if(pic.file.url == photoURL) :
         photo = pic

   #the errors object

   errors = {
       "validArtist":True,
       "validYear":True,
       "validPhoto":True
    }

   
   #cheking the method

   if request.method == "POST" :

      #cheking all the possible artists and photos

      artists = Artist.objects.all()
      photos = Photo.objects.all()

     #function to detect if artist exists

      def artistExists(name) :
       response = False
       for model in artists:
          if model.name == name :
             response = True

       return response
      
      #function to detect if photo exists
     
      def photoExists(name, current) :
       response = False
       for model in photos:
          if model.name == name :
             response = True

       if name == current:
        return False
       else:
         return response


      form = EditPhotoForm(request.POST, request.FILES)

      if form.is_valid():
        
        info = form.cleaned_data
        
        if artistExists(info["artista"]) and not photoExists(info["nombre"], photo.name) and info["año"] > 1700 and info["año"] < 2024:
           
           photo.name = info["nombre"]
           photo.artist = info["artista"]
           if(info["archivo"]):
            photo.file = info["archivo"]
           photo.year = info["año"]
           photo.description = info["descripcion"]
           photo.save()

           return render(request, "editPhoto/editPhoto.html", {"form":form, "errors":errors})
        
        elif not artistExists(info["artista"]):
         errors["validArtist"] = False
         return render(request, "editPhoto/editPhoto.html", {"form":form, "errors":errors})
        
        elif photoExists(info["nombre"], photo.name):
           errors["validPhoto"] = False
           return render(request, "editPhoto/editPhoto.html", {"form":form, "errors":errors})
        
        elif info["año"] < 1700 or info["año"] > 2023:
           errors["validYear"] = False
           return render(request, "editPhoto/editPhoto.html", {"form":form, "errors":errors})
   
   else:
      form = EditPhotoForm(initial = {"nombre":photo.name, "año":photo.year, "archivo":photo.file, "artista":photo.artist, "descripcion":photo.description})

   return render(request, "editPhoto/editPhoto.html", {"form":form, "errors":errors})

@login_required
def deletePhoto(request, photoURL):
   originalURL = unquote(photoURL)

   #getting the real photo URL replacing "%line%" with "/"
   photoURL = unquote(photoURL.replace("%line%", "/"))
   pictures = Photo.objects.all()
   photo = None

   for pic in pictures:
      if(pic.file.url == photoURL) :
         photo = pic


   #checking the method

   if request.method == "POST" and photo != None:
      photo.delete()
   
   return render(request,"singlePhoto/singlePhoto.html", {"photoURL":originalURL,"picture":photo,"delete":True})

def about(request) :
   return render(request,"about/about.html")