from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, login, logout
from django.contrib.auth.models import User
from . import models
# Create your views here.
def home(request):
    ma = User.objects.all().last()
    po = models.post.objects.all().count()
    context = {
        'macs': ma,
        'pots': po,
    }

    return render(request,"home.html",context)

def all(request):
    post = models.post.objects.all().order_by('-id')
    context = {
        'posts':post,
    }
    return render(request,"landing.html",context)
def signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST['uname']
            pass1 = request.POST['psw']
            pass2 = request.POST['psw-repeat']
            if pass1 != pass2:
                messages.error(request,"Password didn't match!")
            else:
                myuser = User.objects.create_user(username=username, password=pass1)
                myuser.is_active=True
                myuser.save()
                return redirect('/login')
        return render(request,"signup.html")
    else:
        return redirect('/')
def lin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['uname']
            pass1 = request.POST['psw']
            user = authenticate(username=username, password=pass1)

            if user is not None:
                print(user)
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Bad Credentials!")
                return redirect('/')

        return render(request,"login.html")
    else:
        return redirect('/')
def lout(request):
    logout(request)
    return redirect('/')
def seepost(request):
    if request.user.is_authenticated:
        posts = models.post.objects.filter(uid=request.user)
        context={

            'posts':posts,
        }
        cnt = models.post.objects.all().count()
        return render(request,"seepost.html",context)


    else:
        return redirect('/')

def createpost(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            title = request.POST['btitle']
            des=request.POST['des']
            # print(request.user.id,title,des)
            post= models.post(uid=request.user,tital=title,des=des)
            post.save()

        return render(request, "createpost.html")
    else:
        return redirect('/')

def update(request, idup):
    if request.user.is_authenticated:
        post=models.post.objects.get(id=idup,uid=request.user)
        print(post)
        if post is not None:

            context={
                'post':post,
            }

            if request.method=='POST':
                post.tital=request.POST['btitle']
                post.des=request.POST['des']
                post.save()
            return render(request,"update.html",context)

        else:
            return redirect('/')
    else:
        return redirect('/')
def delete(request, iddel):
    if request.user.is_authenticated:
        post=models.post.objects.get(id=iddel,uid=request.user)
        print(post)
        if post is not None:

            context={
                'post':post,
            }
            if request.method=='POST':
                post.delete()
                return redirect('/seepost')
            return render(request,"delete.html",context)
        else:
            return redirect('/')
    else:
        return redirect('/')