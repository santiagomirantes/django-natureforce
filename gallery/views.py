from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from gallery.models import *
from gallery.forms import *

def index(request) :


    dict = {
    }

    #rendering it

    return render(request, "index/index.html", dict)

def gallery(request) :
    pictures = Photo.objects.all()
    return render(request, "gallery/gallery.html", {"pictures":pictures})

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
          photo = Photo(name = info["nombre"], year = info["año"], file = info["archivo"], artist = info["artista"])
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


def searchPicture(request) :

   search = request.GET["search"]
   pictures = []
   byName = Photo.objects.filter(name__icontains=search)
   byArtist = Photo.objects.filter(artist__icontains=search)

   pictures.extend(byName) 
   pictures.extend(byArtist)

   pictures = list(set(pictures))
   return render(request, "gallery/gallery.html", {"pictures":pictures})


def account(request):
    return render(request, "account/account.html",{})

def register(request):

   #errors

   errors={
      "isPost":True,
      "userIsValid":True
   }

   #creating a method to check if user exists

   users = User.objects.all()

   def userExists(email) :
       response = False
       for model in users:
          if model.email == email :
             response = True

       return response

   #checking if method is POST

   if request.method == "POST":

      #recieving the form

      form = AddUserForm(request.POST, request.FILES)

      #if the info is valid, recieves it

      if form.is_valid():
         
         info = form.cleaned_data

         if userExists(info["email"]) :

            errors["userIsValid"] = False
         
         else: 
         
            user = User(name = info["nombre"], email = info["email"], profilePicture = info["foto"])
            user.save()

            form = AddUserForm(None)

            return render(request, "register/register.html", {"form":form, "errors":errors})

   else:
      errors["isPost"] = False
      form = AddUserForm()
   
   return render(request,"register/register.html",{"form":form, "errors":errors})

def login(request):
   return render(request, "login/login.html")