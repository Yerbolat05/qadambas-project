from ast import Try
from statistics import mode
from django.db import models
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
