# -*- coding: utf-8 -*-
# Django
from django.urls import path

# Third parties

# Local
from .views import HomeView, ListAllClients, ClientCreateView, ClientUpdateView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('clients', ListAllClients.as_view(), name='clients'),
    path('clients/add', ClientCreateView.as_view(), name='add-clients'),
    path('clients/update/<pk>', ClientUpdateView.as_view(), name='update-clients'),
]