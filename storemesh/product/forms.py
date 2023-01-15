from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import CheckboxInput
from django_countries.fields import CountryField
from .utility import BaseFormInherit
from .models import Product,ProductCategory
class DateInput(forms.DateInput):
    input_type = 'date'
import datetime

#Product Category

# class DateForm(forms.Form,BaseFormInherit):
#     date = forms.DateField()
#     def __init__(self,*args, **kwargs):
#         super(DateForm,self).__init__(*args, **kwargs)
#         self.fields["date"] = forms.DateField(widget=DateInput(format=('%Y-%m-%d'),attrs={'class':'form-control'}), initial=datetime.date.today())

class ProductCategroyForm(forms.ModelForm,BaseFormInherit):
    
    class Meta:
        

        model = ProductCategory
        fields = ['name']
    
    def __init__(self,*args, **kwargs):
        super(ProductCategroyForm,self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = "Enter Category Name"
        

class ProductForm(forms.ModelForm,BaseFormInherit):
  
    class Meta:
        

        model = Product
        fields = ['name','type','category','description','unit_price','slug','image',]
    
    def __init__(self,*args, **kwargs):
        super(ProductForm,self).__init__(*args, **kwargs)

        
        self.fields['name'].widget.attrs['placeholder'] = "Enter Name"
        self.fields['slug'].widget.attrs['placeholder'] = "Fill Slugname"

        self.fields['category'].empty_label = "Select Category"
        self.fields['description'].widget.attrs['placeholder'] = "Please Enter Product Description"
        self.fields['unit_price'].widget.attrs['placeholder'] = "Unit Price"



       





