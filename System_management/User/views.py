from django.shortcuts import redirect,render,HttpResponse
# Create your views here.
from .models import User, Post


def post_add(request):
    if(request.method=="GET"):
        return render(request,"PostAdd.html",{})
    else:
        if("uname" in request.session):
            txt=request.POST["txt"]
            uname=request.session["uname"]
            new_post=Post(user=User(username=uname),text=txt)
            new_post.save()
            return redirect(logout_user) #only loggedin user can post
        else:
            return redirect(login_user)

def register(request):
    if(request.method=="GET"):
        return render(request,"register.html",{})
    else:
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        uname=request.POST["uname"]
        pwd=request.POST["pwd"]
        email=request.POST["email"]

        try:
            new_user=User.objects.get(username=uname)
        except:
            new_user=User(fname,lname,email,pwd,uname)
            new_user.save()
        else:
            #return HttpResponse("User name already exist")
            return redirect(register)
        request.session["uname"]=uname
        return redirect(post_add)

def login_user(request):
    if(request.method=="GET"):
        return render(request,"login.html",{})
    else:
        uname=request.POST["uname"]
        pwd=request.POST["pwd"]
        try:
            new_user=User.objects.get(username=uname,password=pwd)
        except:
            #return HttpResponse("Invalid username or password")
            return redirect(login_user)
        request.session["uname"]=uname
        return redirect(post_add)    
        #return HttpResponse("Login successful")

def logout_user(request):
    request.session.clear()
    return redirect(login_user)
