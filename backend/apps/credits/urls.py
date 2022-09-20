# -*- coding: utf-8 -*-
# Django
from django.urls import path

# Third parties

# Local
from .views import (
    HomeView,
    ListAllClients,
    ClientCreateView,
    ClientUpdateView,
    ClientDeleteView,
    ListAllBanks,
    BankCreateView,
    ListAllCredit,
    CreditCreateView,
)


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('clients', ListAllClients.as_view(), name='clients'),
    path('clients/add', ClientCreateView.as_view(), name='add-clients'),
    path('clients/update/<pk>', ClientUpdateView.as_view(), name='update-clients'),
    path('clients/delete/<pk>', ClientDeleteView.as_view(), name='delete-clients'),
    path('banks', ListAllBanks.as_view(), name='banks'),
    path('banks/add', BankCreateView.as_view(), name='add-banks'),
    path('credits', ListAllCredit.as_view(), name='credits'),
    path('credits/add', CreditCreateView.as_view(), name='add-credits'),
]
