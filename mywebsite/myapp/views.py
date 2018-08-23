from django.shortcuts import render
from myapp.forms import UserForm, UserProfileInfoForm
from django import forms
#
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, 'myapp/index.html')


@login_required
def special(request):
    return HttpResponse("You are logged in,Thanks!")


# wanna make sure user who loging caan logout thats by decoreots
@login_required
def user_logout(request):
    # logout bulit in
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):

    registered = False
    if request.method == "POST":
        # this garp data from user form when user register
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            """ grap user from user_form then save it
                    then hash th password then save it
            """
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            # the additional fields
            """ this won't save directr;y to the database
                and this use the OneToOneField we created
            """
            profile = profile_form.save(commit=False)
            profile.user = user
            """ request.FILES for pdf/img/cv """
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'myapp/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


def user_login(request):

    if request.method == 'POST':
        # get name/password when user post in form
        username = request.POST.get('username')
        password = request.POST.get('password')

        # django authenticate bulit in
        user = authenticate(username=username, password=password)
        # if we have a user check that
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account Not Active")
        else:
            print("someone tried to login and field")
            print("username: {} and password {}".format(username, password))
            return HttpResponse("inviled loging details")
    else:
        return render(request, 'myapp/login.html', {})
