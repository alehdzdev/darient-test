# -*- coding: utf-8 -*-
# Django
from django import forms

# Local
from credits.models import Bank, Client, Credit


class ClientForm(forms.ModelForm):
    """ClientForm for client creation."""

    fullname = forms.CharField(
        label='Nombre y Apellido',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    birthdate = forms.DateField(
        label='Fecha de nacimiento',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
    )
    age = forms.IntegerField(
        label='Edad',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}),
    )
    nationality = forms.CharField(
        label='Nacionalidad', widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    address = forms.CharField(
        label='Direccion de habitacion',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'type': 'email'}),
    )
    telephone = forms.CharField(
        label='Telefono',
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'tel'}),
    )
    type = forms.TypedChoiceField(
        label='Tipo de cliente',
        widget=forms.Select(attrs={'class': 'form-select'}),
        choices=Client.ClientType.choices,
    )
    bank = forms.ModelChoiceField(
        queryset=Bank.objects.all(),
        label='Banco',
        widget=forms.Select(attrs={'class': 'form-select'}),
    )

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
            'bank',
        )


class BankForm(forms.ModelForm):
    """BankForm for bank creation."""

    name = forms.CharField(
        label='Nombre', widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    address = forms.CharField(
        label='Direccion', widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    type = forms.TypedChoiceField(
        label='Tipo de Banco',
        widget=forms.Select(attrs={'class': 'form-select'}),
        choices=Bank.BankType.choices,
    )

    class Meta:
        model = Bank
        fields = ('name', 'address', 'type')


class CreditForm(forms.ModelForm):
    """ClientForm for credit creation."""

    client = forms.ModelChoiceField(
        queryset=Client.objects.all(),
        label='Cliente',
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    description = forms.CharField(
        label='Descripcion', widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    min_pay = forms.DecimalField(
        label='Pago minimo',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}),
    )
    max_pay = forms.DecimalField(
        label='Pago maximo',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}),
    )
    month_deadline = forms.IntegerField(
        label='Plazos',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}),
    )
    bank = forms.ModelChoiceField(
        queryset=Bank.objects.all(),
        label='Banco',
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    type = forms.TypedChoiceField(
        label='Tipo de credito',
        widget=forms.Select(attrs={'class': 'form-select'}),
        choices=Credit.CreditType.choices,
    )

    class Meta:
        model = Credit
        fields = (
            'client',
            'description',
            'min_pay',
            'max_pay',
            'month_deadline',
            'bank',
            'type',
        )
