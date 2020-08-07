from typing import NamedTuple
from django.db import models
from django.db.models.query import QuerySet

class CustomQuerySet(QuerySet):
    def update(self):
        pass

CustomManager = models.Manager.from_queryset(CustomQuerySet)

class Big(models.Model):
    class Small(NamedTuple):
        def __bool__(self):
            pass
