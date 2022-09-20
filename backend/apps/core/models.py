# -*- coding: utf-8 -*-
from django.db import models


class BaseModel(models.Model):
    """Base model.

    Add base fields that could be helpful with API response in all models.
    """

    sort_order = models.PositiveIntegerField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True
