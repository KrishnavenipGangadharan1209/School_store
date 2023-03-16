from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import PlaceOrder
# Create your views here.

def index(request):
    return render(request,'index.html')


def login(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:

            messages.info(request,'invalid info')
            return redirect('login')

    return render(request,'login.html')
def register(request):

    if request.method== 'POST':
        username = request.POST['user_name']
        pass1 = request.POST['user_password']
        pass2 = request.POST['confirm_password']
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')

            else:

                user=User.objects.create_user(username=username,password=pass1)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'password are not same')
            return redirect('register')
        return redirect('/')

    return render(request,'register.html')

def logout(request):

    auth.logout(request)
    return redirect('/')

def purchase(request):
  if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        age = request.POST.get('age')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        department = request.POST.get('department')
        item = request.POST.get('item')
        purpose = request.POST.get('purpose')
        stud = PlaceOrder(name=name,phone=phone,address=address,age=age,email=email,gender=gender,dob=dob,department=department,item=item,purpose=purpose)
        stud.save()
        return redirect('success')
  return render(request, 'purchase.html')

def success(request):
    return render(request, 'my_success_template.html')