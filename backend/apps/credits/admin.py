# -*- coding: utf-8 -*-
# Django
from django.contrib import admin

# Local
from credits.models import Client, Bank, Credit

admin.site.register(Client)
admin.site.register(Bank)
admin.site.register(Credit)
