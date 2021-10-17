from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth.decorators import login_required
from users.models import After10, After12Arts, After12Commerce, After12Science ,After10colleges, After12engcolleges, After12medicolleges,After12commcolleges,After12artscolleges
from .forms import SignUpForm, LoginForm
# Create your views here.

def home(request):
    count=User.objects.count()
    context={
        'count':count,
    }
    return render(request,'home.html',context)
## yeh FUN banaye
def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email= form.cleaned_data.get("email")
            password= form.cleaned_data.get("password")
            try:
                user= User.objects.get(email=email, password=password)
                print(user.email)
                print(user.password)
                return render(request, 'home.html')
            except User.DoesNotExist:
                print("Invalid user!!")
        return redirect('signup')
    else:
        print("method != POST")
        form=  LoginForm()
        context = {
            'form':form,

        }
        return render(request, 'registration/login.html', context)
    

def signup(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=  SignUpForm()
    context = {
        'form':form,
    }
    return render(request,'registration/signup.html',context)

def after10(request):
    questions=After10.objects.all()
    context={
        'questions':questions
    }
    return render(request, 'after10.html',context)


def after12arts(request):
    questions=After12Arts.objects.all()
    context={
        'questions':questions
    }
    return render(request, 'after12.html',context)


def after12commerce(request):
    questions=After12Commerce.objects.all()
    context={
        'questions':questions
    }
    return render(request, 'after12.html',context)

def after12science(request):
    questions=After12Science.objects.all()
    context={
        'questions':questions
    }
    return render(request, 'after12.html',context)

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")


    
def after10colleges(request):
    colleges = After10colleges.objects.all()
    context={
        'colleges':colleges
    }
    return render(request, 'after10colleges.html',context)

    
def after12engcolleges(request):
    colleges = After12engcolleges.objects.all()
    context={
        'colleges':colleges
    }
    return render(request, 'after12engcolleges.html',context)

def after12medicolleges(request):
    colleges = After12medicolleges.objects.all()
    context={
        'colleges':colleges
    }
    return render(request, 'after12medicolleges.html',context)


def after12commcolleges(request):
    colleges = After12commcolleges.objects.all()
    context={
        'colleges':colleges
    }
    return render(request, 'after12commcolleges.html',context)


def after12artscolleges(request):
    colleges = After12artscolleges.objects.all()
    context={
        'colleges':colleges
    }
    return render(request, 'after12artscolleges.html',context)

