# -*- coding: utf-8 -*-
# Django
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.base import TemplateView

# Local
from credits.models import Client
from credits.forms import ClientForm


class HomeView(TemplateView):
    """Home Page for the project."""
    template_name = "credits/home.html"


class ListAllClients(ListView):
    """List View for all the clients."""
    template_name = 'credits/clients/clients_list.html'
    paginate_by = 10
    context_object_name = 'clients'
    queryset = Client.objects.all()


class ClientCreateView(CreateView):
    model = Client
    template_name = "credits/clients/add_client.html"
    form_class = ClientForm
    success_url = reverse_lazy('clients')

    def form_valid(self, form):
        client = form.save()
        client.save()
        return super().form_valid(form)


class ClientUpdateView(UpdateView):
    model = Client
    template_name = "credits/clients/update_client.html"
    form_class = ClientForm
    success_url = reverse_lazy('clients')

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        return super().form_valid(form)