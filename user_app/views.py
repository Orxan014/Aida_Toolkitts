from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from user_app.models import MyUser, TokenModel
from user_app.forms import MyUserCreationForm, Security, MyUserChangeForm
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from user_app.forms import LoginForm


# Create your views here.
def index(request):
    """
    This is home view
    request index url
    """
    return render(request, 'home_page.html')


def register(request):
    """
    This function is
    performed to
    register users.

    """
    context = {'form': MyUserCreationForm()}  # form send to register.html

    if request.method == 'POST':
        # sends the incoming request to the form
        form = MyUserCreationForm(request.POST)

        if form.is_valid():  # if the incoming request is true
            user = form.save(commit=False)  # form save
            # sets passwords.
            user.set_password(form.cleaned_data['password1'])
            user.save()  # the latter saves the process

            return redirect('login')
        else:
            context = {"form": form}

    return render(request, 'register.html', context)


def login_user(request):
    """
        This function is
        performed to
        login users.

    """
    context = {}
    context['form'] = LoginForm()  # empty LoginForm
    if request.method == 'POST':
        # Login Form username and password write
        form = LoginForm(request.POST)
        if form.is_valid():  # if the incoming request is true
            # username example: cavidan_hasanli
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get(
                'password')  # password example: *******
            # If the incoming request authenticate
            user = authenticate(username=username, password=password)
            if user:  # If the incoming request is true

                auth_login(request, user)  # login user

                return redirect('/')  # redirect home url
            else:
                messages.error(
                    request, "Username or Password inValid"
                )  # If user login is not valid error message

                context['form'] = form
    return render(request, 'login.html', context)


def verify_view(request, token, id):
    """
   This function generates
   tokens and
    is used when
    mail is sent
    """
    verify = TokenModel.objects.filter(
        token=token,
        expired=False,
        user_id=id
    ).last()  # genderates token filter
    if verify:
        verify.user.is_active = True
        verify.user.save()
        verify.expired = True
        verify.save()
        return redirect('login')
    else:
        return redirect('index')


def logout_user(request):
    """
            This function is
            performed to
            logout users.

        """
    logout(request)  # user logout
    return redirect("/")


@login_required
def change_password(request):
    """

  This feature helps the
  user to change the user's
  password when they are
  active on the site
"""
    context = {"form": Security()}

    if request.method == "POST":
        form = Security(request.POST)
        if form.is_valid():
            check = request.user.check_password(
                form.cleaned_data.get("CurrentPassword"))
            if check:
                pas1 = form.cleaned_data.get(
                    "Newpassword")  # Change New Password
                # Confrim Changed password
                pas2 = form.cleaned_data.get("ConfirmPassword")
                if pas1 == pas2:  # if match
                    request.user.set_password(form.cleaned_data.get(
                        "Newpassword"))  # set new password to user
                    request.user.save()
                    return redirect('index')
                else:
                    messages.error(request, 'ASDASD')

            else:
                context = {"form": form}

                messages.error(request, "Password Mismatch")
    return render(request, 'change_password.html', context)


def settings_user(request, id):
    """
    This feature allows the user
    to share personal
    information within the site.
    """
    context = {}
    user = MyUser.objects.filter(id=id).last()
    context['form'] = MyUserChangeForm(instance=user)
    if request.method == 'POST':
        form = MyUserChangeForm(
            request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'usr_settings.html', context)
