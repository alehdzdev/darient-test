# -*- coding: utf-8 -*-
# Django
from secrets import choice
from django import forms

# Local
from credits.models import Bank, Client


class ClientForm(forms.ModelForm):
    """ClientForm for client creation."""

    fullname =  forms.CharField(label='Nombre y Apellido', widget=forms.TextInput(attrs={'class': 'form-control'}))
    birthdate = forms.DateField(label='Fecha de nacimiento', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    age = forms.IntegerField(label='Edad', widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}))
    nationality = forms.CharField(label='Nacionalidad', widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='Direccion de habitacion', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'type': 'email'}))
    telephone = forms.CharField(label='Telefono', widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'tel'}))
    type = forms.TypedChoiceField(label='Tipo de cliente', widget=forms.Select(attrs={'class': 'form-select'}), choices=Client.ClientType.choices)
    bank = forms.ModelChoiceField(queryset=Bank.objects.all(), label='Banco', widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = Client
        fields = (
            'fullname',
            'birthdate',
            'age',
            'nationality',
            'address',
            'email',
            'telephone',
            'type',
            'bank'
        )