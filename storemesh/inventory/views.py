from django.shortcuts import render
from django.http.request import HttpRequest
from product.models import Product
from django.http.response import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from inventory.models import Warehouse,Stock
from django.utils import timezone
from django.urls import reverse_lazy
from django import forms
import csv

class WarehouseListView(ListView):

    model = Warehouse
    # paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class WarehouseCreateView(CreateView):
    model = Warehouse
    fields = ['name']
    success_message = "Warehouse successfully added."
    success_url = reverse_lazy('inventory:warehouse-list')


    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super(WarehouseCreateView, self).get_form(form_class)
        for i in form.fields:
            form.fields[i].widget.attrs.update({'class':'form-control'})

        form.fields['name'].widget = forms.TextInput(attrs={'placeholder': 'Enter name','class':'form-control'})
        return form



class WarehouseDetailView(DetailView):
    model = Warehouse
    template_name = "inventory/warehouse_detail.html"


class WarehouseUpdateView(UpdateView):
    model = Warehouse
    fields = ['name']
    success_url = reverse_lazy('inventory:warehouse-list')


    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super(WarehouseUpdateView, self).get_form(form_class)
        for i in form.fields:
            form.fields[i].widget.attrs.update({'class':'form-control'})
        form.fields['name'].widget = forms.TextInput(attrs={'placeholder': 'Enter name','class':'form-control'})
        return form

class WarehouseDeleteView(DeleteView):
    model = Warehouse
    success_url = reverse_lazy('inventory:warehouse-list')

   







    
    












