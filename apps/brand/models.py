from django.db import models
from django.forms import CharField
from django.http import QueryDict
from abstracts.models import (
    AbstractDateTime
)
from django.contrib.auth.models import User
from auths.models import CustomUser
from django.db.models.query import QuerySet

class AccountQuerySet(QuerySet):
    def get_superuser(self) -> QuerySet:
        return self.filter(
            user__is_superuser = True
        )


class Account(AbstractDateTime):
    ACCOUNT_FULL_NAME_MAX_LENGTH = 20
    user = models.OneToOneField(
        CustomUser,
        on_delete = models.CASCADE
    )
    full_name = models.CharField(
        max_length = ACCOUNT_FULL_NAME_MAX_LENGTH,
        verbose_name = 'Аккаунт'
    )
    description = AccountQuerySet().as_manager()

    def __str__(self):
        return f'Аккаунт : {self.user.id} / {self.full_name}'
    
    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'


class ClothesQuerySet(QuerySet):
    def get_not_deleted(self) -> QuerySet:
        return self.filter(
            datetime_deleted__isnull = True
        )


class Clothes(AbstractDateTime):

    IMAGE_TYPES = (
        'png',
        'jpg',
        'jpeg'
    ) 
    TOPIC_SHIRT = 'рубашка'
    TOPIC_SKIRT = 'юбка'
    TOPIC_TROUSERS = 'брюки'
    TOPIC_SHOES = 'обувь'
    TOPIC_CAP = 'кепка'
    TOPIC_SOCKS = 'носки'

    TOPIC_CHOICES_ONE = (
        {TOPIC_SHIRT,'Рубашка'},
        {TOPIC_SKIRT,'Юбка'},
        {TOPIC_TROUSERS,'Брюки'},
        {TOPIC_SHOES,'Обувь'},
        {TOPIC_CAP,'Кепка'},
        {TOPIC_SOCKS,'Носки'},
    )

    TOPIC_GUCCI = 'gucci'
    TOPIC_ARMANI = 'armani'
    TOPIC_NIKE = 'nike'
    TOPIC_PRADA = 'prada'
    TOPIC_QR = 'qazaq republic'
    TOPIC_ADIDAS = 'adidas'
    TOPIC_FENDI = 'fendi'
    TOPIC_DIOR = 'dior'
    TOPIC_LV = 'louis vuitton'
    TOPIC_THRASHER = 'thrasher'

    TOPIC_CHOICES_TWO = (
        {TOPIC_GUCCI,'Gucci'},
        {TOPIC_ARMANI,'Armani'},
        {TOPIC_NIKE,'Nike'},
        {TOPIC_PRADA,'Prada'},
        {TOPIC_QR,'Qazaq Republic'},
        {TOPIC_ADIDAS,'Adidas'},
        {TOPIC_FENDI,'Fendi'},
        {TOPIC_DIOR,'Dior'},
        {TOPIC_LV,'Louis Vuitton'},
        {TOPIC_THRASHER,'Thrasher'}
    )

    user = models.ForeignKey(
        CustomUser, on_delete=models.PROTECT,
        verbose_name = 'Пользователь'
    )

    name = models.CharField(
        max_length = 150,
        verbose_name = 'Название'
    )

    brand = models.CharField(
        max_length = 50,
        choices = TOPIC_CHOICES_TWO,
        verbose_name = 'Брэнд'
    )

    img = models.ImageField(
        upload_to = 'clothes/',
        max_length = 255
    )
    country = models.CharField(
        max_length = 50,
        verbose_name = 'Пройзводство'
    )

    size = models.IntegerField(
        verbose_name = 'Размер'
    )

    type_clothes = models.CharField(
        max_length = 150,
        verbose_name = 'Ткань'
    )

    categories = models.CharField(
        max_length = 150,
        verbose_name = 'Категория',
        choices = TOPIC_CHOICES_ONE,
        default = TOPIC_SHIRT
    )

    price = models.IntegerField(
        verbose_name = 'Стоймость'
    )

    def __str__(self) -> str:
        return f'Названия товара : {self.name} -- Стоймость : {self.price}'

    objects = ClothesQuerySet().as_manager()

    class Meta:
        ordering = (
            'name',
        )
        verbose_name = 'Одежда'
        verbose_name_plural = 'Одежды'


class Categories(AbstractDateTime):

    FULL_NAME_MAX_LENGTH = 20

    TOPIC_SHIRT = 'Рубашка'
    TOPIC_SKIRT = 'Юбка'
    TOPIC_TROUSERS = 'Брюки'
    TOPIC_SHOES = 'Обувь'
    TOPIC_CAP = 'Кепка'
    TOPIC_SOCKS = 'Носки'

    TOPIC_CHOICES = (
        {TOPIC_SHIRT,'Рубашка'},
        {TOPIC_SKIRT,'Юбка'},
        {TOPIC_TROUSERS,'Брюки'},
        {TOPIC_SHOES,'Обувь'},
        {TOPIC_CAP,'Кепка'},
        {TOPIC_SOCKS,'Носки'},
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категорий'


class Brand(AbstractDateTime):
    FULL_NAME_MAX_LENGTH = 30

    TOPIC_GUCCI = 'Gucci'
    TOPIC_ARMANI = 'Armani'
    TOPIC_NIKE = 'Nike'
    TOPIC_PRADA = 'Prada'
    TOPIC_QR = 'Qazaq Republic'
    TOPIC_ADIDAS = 'Adidas'
    TOPIC_FENDI = 'Fendi'
    TOPIC_DIOR = 'Dior'
    TOPIC_LV = 'Louis Vuitton'

    TOPIC_CHOICES = (
        {TOPIC_GUCCI,'Gucci'},
        {TOPIC_ARMANI,'Armani'},
        {TOPIC_NIKE,'Nike'},
        {TOPIC_PRADA,'Prada'},
        {TOPIC_QR,'Qazaq Republic'},
        {TOPIC_ADIDAS,'Adidas'},
        {TOPIC_FENDI,'Fendi'},
        {TOPIC_DIOR,'Dior'},
        {TOPIC_LV,'Louis Vuitton'},
    )

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'