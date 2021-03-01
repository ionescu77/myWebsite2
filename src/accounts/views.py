from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )

from django.shortcuts import render, redirect, HttpResponseRedirect

from .forms import UserLoginForm


def login_view(request):
    title = "Login"
    next_page = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if request.user.is_authenticated:
        print(request.user.is_authenticated)
        # return redirect("/blog/")
        return render(request, "lockout.html", {"title": title})
    elif form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if username and password:
            if not user:
                return render(request, "lockout.html", {"title": title})
            if not user.check_password(password):
                # raise exceptions.AuthenticationFailed(_('Invalid username/password.'))
                return render(request, "lockout.html", {"title": title})
            if not user.is_active:
                # raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))
                return render(request, "lockout.html", {"title": title})
        login(request, user)
        if next_page:
            return HttpResponseRedirect(next_page)
        return HttpResponseRedirect("/blog/")
    return render(request, "auth_form.html", {"form":form, "title": title})

def register_view(request):
    return render(request, "auth_form.html", {})

def logout_view(request):
    title = "Restricted"
    next_page = request.GET.get('next')
    logout(request)
    if next_page:
        return HttpResponseRedirect(next_page)
    return render(request, "lockout.html", {"title": title})
