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


@login_required
def messages(request):

    received = Message.objects.filter(receiver=request.user.username)
    rlength = len(received)
    sent = Message.objects.filter(transmitter=request.user.username)
    slength = len(sent)


    totalMessages = received[:]
    totalMessages.extend(sent)

    for i in totalMessages:
       i.pos = totalMessages.index(i)

    return render(request,"messages/messages.html", {"received":received,"sent":sent, "rlen":rlength, "slen":slength})

@login_required
def newMessage(request):
   
   errors = {
      "success":False,
      "userExists":True
   }
   
   if request.method == "POST":
      
      #creating a method to check if user exists

      def userExists(username):
         try:
           user = User.objects.get(username=username)
           return True
         except User.DoesNotExist:
           return False
      
      form = newMessageForm(request.POST)

      if form.is_valid():
         
         info = form.cleaned_data

         if userExists(info["receiver"]):

            newMessage = Message(receiver=info["receiver"],transmitter=request.user.username,title=info["title"], content=info["content"])

            newMessage.save()

            errors["success"] = True

            form = newMessageForm()

         else:

            errors["userExists"] = False

      return render(request, "newMessage/newMessage.html", {"form":form, "errors":errors})
    
   else:
      
      form = newMessageForm()

   return render(request, "newMessage/newMessage.html", {"form":form, "errors":errors})


@login_required
def singleMessage(request, mesPos) :
   
   received = list(Message.objects.filter(receiver=request.user.username))
   sent = list(Message.objects.filter(transmitter=request.user.username))

   totalMessages = received[:]
   totalMessages.extend(sent)

   message = totalMessages[int(mesPos)]

   isReceived = False

   if int(mesPos) <= len(received) - 1:
      isReceived = True
   
   return render(request, "singleMessage/singleMessage.html", {"message":message, "isReceived":isReceived})