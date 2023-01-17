import django
from product.models import Product
from customer.models import Customer
from django import forms
from django.db.models import fields
from .models import SaleOrder,SaleOrderLine
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from .custom_layout_objects import *
from customer.models import Customer
from django.forms import widgets
import datetime

class DateInput(forms.DateInput):
    input_type = 'date'

from django.forms import BaseInlineFormSet

class BaseSaleOrderLine(BaseInlineFormSet):
    def __init__(self, other_model_queryset, *args, **kwargs):
        super(BaseSaleOrderLine, self).__init__(*args, **kwargs)
        for form in self.forms:
            form.fields['product'].queryset = other_model_queryset

class SaleOrderLineForm(forms.ModelForm):

    class Meta:
        model = SaleOrderLine
        exclude = ()
    
    def __init__(self, *args, **kwargs):
        super(SaleOrderLineForm, self).__init__(*args, **kwargs)
    
#passing formset additionally to work with inline formset 

SaleOrderLineFormSet = inlineformset_factory(
    SaleOrder, SaleOrderLine, form=SaleOrderLineForm,
    fields=['product', 'quantity'], extra=1, can_delete=True,formset=BaseSaleOrderLine
    )



class SalOrderForm(forms.ModelForm):

    class Meta:
        model = SaleOrder
        fields="__all__"

    def __init__(self, *args, **kwargs):
        super(SalOrderForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs.update({'class':'form-control'})
        
        self.fields["order_date"] = forms.DateField(widget=DateInput(format=('%Y-%m-%d'),attrs={'class':'form-control'}), initial=datetime.date.today())
        self.fields['buyer'].queryset = Customer.objects.all()
        
        # self.fields["vendor"].queryset = Customer.objects.filter(is_vendor=True)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        if self.instance.id is not None:
          
            self.helper.layout = Layout(
                Div(
                    Field('ref',readonly="True"),
                    Field('order_date'),
                    Field('buyer'),
                    Field('status'),
                    
                        
                  




                    Fieldset('Create So !! dont duplicate product',
                        Formset('titles')),
                    
                    HTML("<br>"),
                    ButtonHolder(Submit('submit', 'Update')),
                    )
                )
        else:
            self.helper.layout = Layout(
                Div(
                    
                    Field('order_date'),
                    Field('buyer'),
                    Field('status'),




                    Fieldset('Create So Lines !! dont duplicate product',
                        Formset('titles')),
                    
                    HTML("<br>"),
                    ButtonHolder(Submit('submit', 'save')),
                    )
                )