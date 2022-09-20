# -*- coding: utf-8 -*-
# Django
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Local
from credits.models import Client, Bank, Credit
from credits.forms import ClientForm, BankForm, CreditForm


class HomeView(TemplateView):
    """Home Page for the project."""

    template_name = 'credits/home.html'


# Clients
class ListAllClients(ListView):
    """List View for all the clients."""

    template_name = 'credits/clients/list_client.html'
    paginate_by = 10
    context_object_name = 'clients'
    queryset = Client.objects.all()


class ClientCreateView(CreateView):
    """ClientCreate View with ClientForm as form class."""

    model = Client
    template_name = 'credits/clients/add_client.html'
    form_class = ClientForm
    success_url = reverse_lazy('clients')

    def form_valid(self, form):
        client = form.save()
        client.save()
        return super().form_valid(form)


class ClientUpdateView(UpdateView):
    """ClientUpdate View with ClientForm as form class."""

    model = Client
    template_name = 'credits/clients/update_client.html'
    form_class = ClientForm
    success_url = reverse_lazy('clients')

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        return super().form_valid(form)


class ClientDeleteView(DeleteView):
    """ClientDelete View."""

    model = Client
    template_name = 'credits/clients/delete_client.html'
    success_url = reverse_lazy('clients')


# Banks
class ListAllBanks(ListView):
    """List View for all the banks."""

    template_name = 'credits/banks/list_bank.html'
    paginate_by = 10
    context_object_name = 'banks'
    queryset = Bank.objects.all()


class BankCreateView(CreateView):
    """Bank Create View."""

    model = Bank
    template_name = 'credits/banks/add_bank.html'
    form_class = BankForm
    success_url = reverse_lazy('banks')

    def form_valid(self, form):
        client = form.save()
        client.save()
        return super().form_valid(form)


# Credit
class ListAllCredit(ListView):
    """List View for all the credit."""

    template_name = 'credits/credits/list_credit.html'
    paginate_by = 10
    context_object_name = 'credits'
    queryset = Credit.objects.all()


class CreditCreateView(CreateView):
    """Credit Create View."""

    model = Credit
    template_name = 'credits/credits/add_credit.html'
    form_class = CreditForm
    success_url = reverse_lazy('credits')

    def form_valid(self, form):
        client = form.save()
        client.save()
        return super().form_valid(form)
