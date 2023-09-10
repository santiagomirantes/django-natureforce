from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from accounts.forms import *
from accounts.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def account(request):

    avatar = None
    user = None
    if request.user.is_authenticated :

     try:
      avatar = Avatar.objects.get(user=request.user.id)
     except Avatar.DoesNotExist:
      avatar = None

     user = request.user
    return render(request,"account/account.html", {"avatar":avatar,"user":user})

def loginView(request):

    errors = {
        "validUser":True
    }

    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)

            if user is not None:
                
                login(request,user)

                avatar = None
                user = None
                if request.user.is_authenticated :

                 try:
                    avatar = Avatar.objects.get(user=request.user.id)
                 except Avatar.DoesNotExist:
                    avatar = None

                return render(request, "account/account.html", {"avatar":avatar,"errors":errors})
            
            else:
                errors.validUser = False
                return render(request,"login/login.html",{"errors":errors})
            
    form = AuthenticationForm()
    
    return render(request,"login/login.html", {"form":form, "errors":errors})

def registerView(request):

    errors = {

    }

    if request.method == "POST":

        form = UserRegisterForm(request.POST, request.FILES)

        if form.is_valid():

            username = form.cleaned_data["username"]

            form.save()

            user = User.objects.get(username=username)

            avatar = Avatar(user=user,image=form.cleaned_data["avatar"])
            avatar.save()

            return render(request, "account/account.html")
        
    else:
            form = UserRegisterForm()

    return render(request, "register/register.html", {"form":form, "errors":errors})

@login_required
def editProfile(request):

    user = request.user

    if request.method == "POST":

       form = UserEditForm(request.POST,request.FILES,instance=user)

       if form.is_valid():
           info = form.cleaned_data
           user.email = info["email"]
           if info["password1"]:
                user.set_password(info["password1"])
           user.save()

           # Check if a new avatar image has been uploaded
           if 'avatar' in request.FILES:
           
                try:
                    avatar = Avatar.objects.get(user=user)
                    avatar.delete()
                except Avatar.DoesNotExist:
                    pass  # No existing avatar found, do nothing

                newAvatar = Avatar(user=user, image=request.FILES['avatar'])
                newAvatar.save()

           return render(request,"editProfile/editProfile.html", {"form":form,"success":True})
       
    else:
        try:
         avatar = Avatar.objects.get(user=request.user.id)
        except Avatar.DoesNotExist:
         avatar = None
        form = UserEditForm(instance=user)
        #initial={"username":user.username,"email":user.email, "avatar":avatar}

    return render(request, "editProfile/editProfile.html", {"form":form, "success":False})


def messages(request):
    return render(request,"messages/messages.html")