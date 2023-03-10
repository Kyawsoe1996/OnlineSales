from django.db.models import query
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from .models import SaleOrder,SaleOrderLine
from .forms import SaleOrderLineForm,SaleOrderLineFormSet,SalOrderForm
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.db import transaction
from django.http import HttpResponse
from django import forms
import datetime
from django.forms import widgets
from .models import STATUS
from product.models import Product
from customer.models import Customer
from django.contrib.auth.mixins import LoginRequiredMixin
from inventory.models import Stock





def create_so_num():
        code = 'SO '
        month =datetime.date.today().month
        day = datetime.date.today().day
        year = datetime.date.today().year
        format_str = "%s/%s/%s---" % (day,month,year)
        
        if SaleOrder.objects.all().count() == 0:
            so_max_id = 0
        else:
            so_max_id = SaleOrder.objects.all().order_by("-id")[0].id
        
        so_code = code + format_str +str(so_max_id + 1)
        return so_code

def SaleListView(request):
    so_lists = SaleOrder.objects.all()
    context = {
        "so_lists":so_lists
    }
    return render(request,"sale/sale_list.html",context)

class DateInput(forms.DateInput):
    input_type = 'date'


class SaleOrderCreate(LoginRequiredMixin,CreateView):
    model = SaleOrder
    template_name = 'sale/sale_create.html'
    form_class = SalOrderForm
    # success_url = None
    success_url = reverse_lazy('sale:sale-list')
   
    def get_context_data(self, **kwargs):
        data = super(SaleOrderCreate, self).get_context_data(**kwargs)
        queryset = Product.objects.all()
        if self.request.POST:
                data['titles'] = SaleOrderLineFormSet(queryset,self.request.POST)
        else:
            #https://stackoverflow.com/questions/19305964/change-queryset-of-model-field-in-inlineformset-of-non-parent-model 


            data['titles'] = SaleOrderLineFormSet(queryset)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        titles = context['titles']
        with transaction.atomic():
            # form.instance.created_by = self.request.user
            self.object = form.save(commit=False)
            self.object.ref = create_so_num()
            #when so created after google login customer, saved only with that user
            # #TODO######
            # need to show in only that customer in SaleOrder Form
            #################
            self.object.buyer= self.request.user.customer 
            self.object.save()
            if titles.is_valid():
                
                for  form in titles:
                    so_line_obj = form.save(commit=False)

                    so_line_obj.sub_total = so_line_obj.get_subtotal()

                    so_line_obj.sale_order = self.object

                    so_line_obj.save()
                    ##.....To update the stock............
                    product_obj = so_line_obj.product
                    try:
                        stock = Stock.objects.get(product_id=product_obj)
                    except:
                        return HttpResponse("U don't add current stock for the product yet.. Choose the product the have the stock")
                    stock.quantity -= so_line_obj.quantity
                    stock.save()
                    product_obj.qty_in_warehouse_stocks = product_obj.get_current_stocks()
                    product_obj.save()
                    # ..............................................


            self.object.total_price = self.object.sale_order_total()
            self.object.save()
        return super(SaleOrderCreate, self).form_valid(form)



class SaleDetailView(DetailView):
    model = SaleOrder
    template_name = "sale/sale_detail.html"

    def get_context_data(self, **kwargs):
        context = super(SaleDetailView, self).get_context_data(**kwargs)
        context['status'] = STATUS
        return context



class SaleUpdateView(UpdateView):
    model = SaleOrder
    form_class = SalOrderForm
    template_name = 'sale/sale_create.html'
    success_url = reverse_lazy('sale:sale-list')


    def get_context_data(self, **kwargs):
        data = super(SaleUpdateView, self).get_context_data(**kwargs)
        queryset = Product.objects.all()

        if self.request.POST:
            data['titles'] = SaleOrderLineFormSet(queryset,self.request.POST, instance=self.object)
        else:
                data['titles'] = SaleOrderLineFormSet(queryset,instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        titles = context['titles']
        with transaction.atomic():
            # form.instance.created_by = self.request.user
            self.object = form.save(commit=False)
            #when so created after google login customer, saved only with that user
            # #TODO######
            # need to show in only that customer in SaleOrder Form
            #################
            self.object.buyer = self.request.user.customer
            self.object.save()

            
            titles.save()
            for so_line in self.object.so_lines.all():
                # so_line.sub_total = so_line.get_subtotal()
                so_line.sub_total = so_line.get_subtotal()

                so_line.save()
                ##.....To update the stock............
                product_obj = so_line.product
                try:
                    stock = Stock.objects.get(product_id=product_obj)
                except:
                    return HttpResponse("U don't add current stock for the product yet.. Choose the product the have the stock")
                stock.quantity -= so_line.quantity
                stock.save()
                product_obj.qty_in_warehouse_stocks = product_obj.get_current_stocks()
                product_obj.save()
                # ..............................................

            self.object.total_price = self.object.sale_order_total()
            self.object.save()
          
        return super(SaleUpdateView, self).form_valid(form)

   