from typing import Optional

from django.db.models import QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import (
    authenticate as dj_authenticate,
    login as dj_login,
    logout as dj_logout
)
from django.views import View

from abstracts.mixins import HttpResponseMixin
from abstracts.handlers import ViewHandler
from apps.brand.forms import CreatedClothes
from auths.models import CustomUser
from auths.forms import CustomUserForm
from .models import (
    Clothes,
)

class IndexView(ViewHandler,View):
    
    """Index View"""

    queryset: QuerySet = \
        Clothes.objects.get_not_deleted()

    def get(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict
    ) -> HttpResponse:
        """GET request handler"""

        response: Optional[HttpResponse] = \
            self.get_validated_response(
                request
            )

        if response:
            return response

        if not request.user.is_authenticated:
            return render(
                request,
                'brand/index.html'
            )

        clothes : QuerySet = self.queryset.filter(
            user = request.user
        )

        if not clothes:
            clothes = self.queryset
            
        context: dict = {
            'ctx_title' : 'Kiumdy',
            'ctx_clothes' : clothes,
        }
        template_name : str = 'brand/index.html'

        return self.get_http_response(
            request,
            template_name,
            context
        )

class RegisterView(ViewHandler,View):
    pass


class LoginView(ViewHandler,View):
    pass


class LogoutView(ViewHandler,View):
    pass


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


class CreatePostView(ViewHandler,View):

    """Post Create View."""

    form: CreatedClothes = CreatedClothes
    template_name: str = 'brand/created.html'

    def get(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict
    ) -> HttpResponse:
        """GET request handler"""

        response: Optional[HttpResponse] = \
            self.get_validated_response(
                request
            )
        if response:
            return response

        context: dict = {
            'form' : self.form
        }

        return self.get_http_response(
            request,
            self.template_name,
            context
        )
    
    def post(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwarga: dict
    ) -> HttpResponse:
        """POST request handler"""

        form: CreatedClothes = self.form(
            request.POST,
            request.FILES
        )
        if not form.is_valid():
            context: dict = {
                'form' : form
            }
            return self.get_http_response(
                request,
                self.template_name,
                context
            )
        clothes: Clothes = form.save(
            commit=False
        )
        clothes.user = request.user
        clothes.img = request.FILES['img']

        file_type: str = clothes.img.url.split('.')[-1].lower()

        if file_type not in Clothes.IMAGE_TYPES:

            context: dict = {
                'form' : form,
                'ctx_clothes' : clothes,
                'error_message' : 'PNG, JPG, JPEG'
            }
            return self.get_http_response(
                request,
                self.template_name,
                context
            )
        clothes.save()

        context: dict = {
            'clothes' : clothes
        }
        template_name : str = 'brand/detail.html'
        return self.get_http_response(
            request,
            template_name,
            context
        )


def brand(request: WSGIRequest) -> HttpResponse:
    context : dict = {
        'ctx_title' : 'Kiumdy'
    }
    return render(
        request,
        template_name = 'brand/brand.html',
        context = context
    )