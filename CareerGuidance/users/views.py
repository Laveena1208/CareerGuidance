

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


# def login(request):
#     return render(request, 'login.html')
    # return HttpResponse("hello")

def login(request):
    if request.method == 'GET':
        return render(request,"login.html")

    if request.method == 'POST':
        form = request.form
        username = form.get('username', None)
        password = form.get('password', None)
        if(Users.exists(username)):
            user = Users.get_user_by_username(username)
            if (check_password_hash(user.password, password)):
                session['user'] = user.id
                flash("You are Logged in", "success")
                response = make_response(redirect(url_for('home')))
            else:
                flash("Incorrect Password", "info")
                return redirect(url_for('login'))
        else:
                flash("Incorrect user credentials", "info")
                return redirect(url_for('login'))

def register(request):
    if request.method == 'GET':
        return render("register.html")
    elif request.method == 'POST':
        form = request.form
        name = form.get('name',None)
        username = form.get('username',None)
        password = form.get('password',None)
        if (username and name and password):
            if(not Users.exists(username)):
                password = generate_password_hash(password)
                user = Users(username,password,name)
                flash(f"{username} registered.\n Login to procced","success")
                return redirect(url_for("login"))
            else:
                flash(f"{username} registered.\n already exit","danger")
                return redirect(url_for("register"))
        else:
            flash("Please fill all the details","warning")
            return redirect(url_for("register"))


def register(request):
    return render(request, 'register.html')

def home(request):
    return render(request, 'home.html')

    