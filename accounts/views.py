from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import login, authenticate, logout


# Create your views here.
def login_view(request):
    ("LOGIN")
    ("Login")
    ("Phone Number*")
    ("Password*")

    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('/')

    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            phone = request.POST['phone']
            password = request.POST['password']
            user = authenticate(phone=phone, password=password)
            if user:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Try again")
        else:
            messages.error(request, "Phone number & Password doesn't match!")
    else:
        form = LoginForm()

    context = {"login_form": form}
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')


def signup_view(request):

    ("REGISTER")
    ("Name*")
    ("Phone*")
    ("Email Address")
    ("Address")
    ("Register")

    ("If you want to join as a seller, please select a Producer Organization.")
    ("Enter the same password as before, for verification.")
    ("Required. Add a valid phone number")
    ("Your password can't be too similar to your other personal information.")
    ("Your password must contain at least 8 characters.")
    ("Your password can't be a commonly used password.")
    ("Your password can't be entirely numeric.")

    context = {}
    if not request.user.is_authenticated:
        if request.POST:
            form = RegistrationForm(request.POST)

            if form.is_valid():
                name = form.cleaned_data.get('name')
                phone = form.cleaned_data.get('phone')
                email = form.cleaned_data.get('email')
                raw_password = form.cleaned_data.get('password1')
                form.save(commit=True)
                account = authenticate(name=name, phone=phone, email=email, password=raw_password)
                login(request, account)
                return render(request, 'pages/home.html')
            else:
                context['registration_form'] = form
        else:  # GET request
            form = RegistrationForm()
            context = {
                "registration_form": form
            }
        return render(request, 'signup.html', context)
    else:
        # return render(request, 'registration.html', context)
        return render(request, 'pages/home.html')
