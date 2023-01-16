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
from product.models import Product
from django.forms import inlineformset_factory
from .forms import StockForm

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



StockFormSet = inlineformset_factory(
    Warehouse, Stock, form=StockForm,
    extra=2, can_delete=True, can_delete_extra=True
)
def add_stock_to_warehouse(request,pk):
    try:
        warehouse = Warehouse.objects.get(id=pk)
    except:
        return HttpResponse("Not a valid warehouse")

    if request.method == 'GET':
        formset = StockFormSet()
        context = {
            "formset":formset
        }
        return render(request,'stock/index.html',context=context)
    else:
        formset = StockFormSet(request.POST)
        if formset.is_valid():
            chapters = formset.save(commit=False)
            for chapter in chapters:
                chapter.warehouse = warehouse
                chapter.save()
            
        return redirect("inventory:stock-list")


class StockListView(ListView):
    model = Stock
    template_name= 'stock/stock_list.html'


class StockCreateView(CreateView):
    model = Stock
    fields = ['warehouse','product_id','quantity']
    success_message = "Stock Has been Added Successfully."
    success_url = reverse_lazy('inventory:stock-list')
    template_name = 'stock/stock_form.html'

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super(StockCreateView, self).get_form(form_class)
        for i in form.fields:
            form.fields[i].widget.attrs.update({'class':'form-control'})

        form.fields['quantity'].widget = forms.TextInput(attrs={'placeholder': 'Enter Qty','class':'form-control'})
        # form.fields['warehouse'].widget = forms.TextInput(attrs={'placeholder': 'Enter name','class':'form-control'})
        form.fields["warehouse"].queryset = Warehouse.objects.all()
        form.fields["warehouse"].label = 'Warehouse'
        form.fields["product_id"].label = 'Product'



        return form


class StockUpdateView(UpdateView):
    model = Stock
    fields = ['warehouse','product_id','quantity']
    success_url = reverse_lazy('inventory:stock-list')
    template_name = 'stock/stock_form.html'

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super(StockUpdateView, self).get_form(form_class)
        for i in form.fields:
            form.fields[i].widget.attrs.update({'class':'form-control'})

        form.fields['quantity'].widget = forms.TextInput(attrs={'placeholder': 'Enter Qty','class':'form-control'})
        # form.fields['warehouse'].widget = forms.TextInput(attrs={'placeholder': 'Enter name','class':'form-control'})
        form.fields["warehouse"].label = 'Warehouse'
        form.fields["product_id"].label = 'Product'

        return form


class StockDetailView(DetailView):
    model = Stock
    template_name = "stock/stock_detail.html"

class StockDeleteView(DeleteView):
    model = Stock
    success_url = reverse_lazy('inventory:stock-list')
    template_name = 'stock/stock_confirm_delete.html'


    





   







    
    












