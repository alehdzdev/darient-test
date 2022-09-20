# -*- coding: utf-8 -*-
# Django
from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

# Local
from core.models import BaseModel


class Bank(BaseModel):
    """Bank Model."""

    class BankType(models.TextChoices):
        PRIVATE = 'Privado', _('Privado')
        PUBLIC = 'Gobierno', _('Gobierno')

    name = models.CharField(_('Nombre'), max_length=100)
    type = models.CharField(_('Tipo'), max_length=100, choices=BankType.choices)
    address = models.CharField(_('Direccion'), max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = _('Banco')
        verbose_name_plural = _('Bancos')

    def __str__(self):
        return f'{self.name}'


class Client(BaseModel):
    """Client Model."""

    class ClientType(models.TextChoices):
        NATURAL = 'Natural', _('Natural')
        JURIDICAL = 'Juridico', _('Juridico')

    fullname = models.CharField(_('Nombre y Apellido'), max_length=200)
    birthdate = models.DateField(_('Fecha de Nacimiento'), auto_now=False, auto_now_add=False)
    age = models.PositiveIntegerField(
        _('Edad'),
        blank=True,
        null=True,
        validators=[MaxValueValidator(99), MinValueValidator(1)]
    )
    nationality = models.CharField(_('Nacionalidad'), max_length=100, blank=True, null=True)
    address = models.CharField(_('Direccion de habitacion'), max_length=100, blank=True, null=True)
    email = models.EmailField(_('Email'), max_length=200)
    telephone = models.CharField(_('Telefono'), max_length=50, blank=True, null=True)
    type = models.CharField(_('Tipo'), max_length=100, choices=ClientType.choices)
    bank = models.ForeignKey(Bank,verbose_name=_('Banco'), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Cliente')
        verbose_name_plural = _('Clientes')

    def __str__(self):
        return f'{self.fullname}'


class Credit(BaseModel):
    """Credit model."""

    class CreditType(models.TextChoices):
        AUTOMOTIVE = 'Automotriz', _('Automotriz')
        MORTGAGE = 'Hipotecario', _('Hipotecario')
        COMMERCIAL = 'Comercial', _('Comercial')

    client = models.ForeignKey(Client, verbose_name=_('Cliente'), on_delete=models.CASCADE)
    description = models.CharField(_('Descripcion del Credito'), max_length=200)
    min_pay = models.DecimalField(_('Pago Minimo'), max_digits=10, decimal_places=2)
    max_pay = models.DecimalField(_('Pago Maximo'), max_digits=10, decimal_places=2)
    month_deadline = models.PositiveIntegerField(_('Plazos'))
    date = models.DateField(_('Fecha de registro'), auto_now=False, auto_now_add=True)
    bank = models.ForeignKey(Bank, verbose_name=_('Banco'), on_delete=models.CASCADE)
    type = models.CharField(_('Tipo'), max_length=100, choices=CreditType.choices)

    class Meta:
        verbose_name = _('Credito')
        verbose_name_plural = _('Creditos')

    def __str__(self):
        return f'{self.client.fullname} - {self.bank.name} - {self.type}'
