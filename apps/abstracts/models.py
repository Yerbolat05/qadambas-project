import uuid
from django.db import models

class AbstractDateTime(models.Model):
    datetime_created = models.DateTimeField(
        verbose_name = 'время создание',
        auto_now_add = True
    )

    datetime_updated = models.DateTimeField(
        verbose_name = 'время обновление',
        auto_now = True
    )

    datetime_deleted = models.DateTimeField(
        verbose_name = 'время удаление',
        null = True,
        blank = True
    )

    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)

    class Meta:
        abstract = True
