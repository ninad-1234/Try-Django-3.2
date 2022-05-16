from django.db import models

# Create your models here.
def login_view(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)

    return render(request, "accounts/login.html",{})

def logout_view(request):
    return render(request, "accounts/logout.html",{})

def register_view(request):   
    return render(request, "accounts/register.html",{})        