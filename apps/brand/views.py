from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from auths.models import CustomUser
from auths.forms import CustomUserForm


from django.contrib.auth import (
    authenticate as dj_authenticate,
    login as dj_login,
    logout as dj_logout
)

def index(request: WSGIRequest) -> HttpResponse:

    if not request.user.is_authenticated:
        return render(
            request,
            'brand/login.html'
        )

    context: dict = {
        'ctx_title' : 'Главная страница',
    }
    return render(
        request,
        template_name = 'brand/index.html',
        context = context
    )


def register(request: WSGIRequest) -> HttpResponse:

    form: CustomUserForm = CustomUserForm(
        request.POST
    )
    if form.is_valid():
        user: CustomUser = form.save(
            commit = False
        )
        login: str = form.cleaned_data['login']
        email: str = form.cleaned_data['email']
        password: str = form.cleaned_data['password']
        user.email = email
        user.set_password(password)
        user.save()

        user: CustomUser = dj_authenticate(
            email = email,
            password = password,
            login = login
        )
        if user and user.is_active:

            dj_login(request, user)

            return render(
                request,
                'brand/index.html'
            )
    context: dict = {
        'form': form
    }
    return render(
        request,
        'brand/register.html',
        context
    )


def login(request: WSGIRequest) -> HttpResponse:
    if request.method == 'POST':
        email: str = request.POST['email']
        password: str = request.POST['password']

        user: CustomUser = dj_authenticate(
            email = email,
            password = password
        )

        if not user:
            return render(
                request,
                'brand/login.html',
                {'error_message' : 'Неверные данные'}
            )
        if not user.is_active:
            return render(
                request,
                'brand/login.html',
                {'error_message' : 'Ваш аккаунт был удален'}
            )
        dj_login(request, user)

        return render(
            request,
            'brand/index.html'
        )
    return render(
        request,
        'brand/login.html'
    )


def logout(request: WSGIRequest) -> HttpResponse:

    dj_logout(request)

    form: CustomUserForm = CustomUserForm(
        request.POST
    )
    context: dict = {
        'form' : form,
    }
    return render(
        request,
        'brand/login.html',
        context
    )