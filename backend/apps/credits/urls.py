# -*- coding: utf-8 -*-
# Django
from django.urls import path
from django.contrib.auth.decorators import login_required

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
    path('clients', login_required(ListAllClients.as_view()), name='clients'),
    path('clients/add', login_required(ClientCreateView.as_view()), name='add-clients'),
    path(
        'clients/update/<pk>',
        login_required(ClientUpdateView.as_view()),
        name='update-clients',
    ),
    path(
        'clients/delete/<pk>',
        login_required(ClientDeleteView.as_view()),
        name='delete-clients',
    ),
    path('banks', login_required(ListAllBanks.as_view()), name='banks'),
    path('banks/add', login_required(BankCreateView.as_view()), name='add-banks'),
    path('credits', login_required(ListAllCredit.as_view()), name='credits'),
    path('credits/add', login_required(CreditCreateView.as_view()), name='add-credits'),
]
