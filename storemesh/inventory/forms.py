from django import forms

from .models import Stock
class StockForm(forms.ModelForm):
    
    class Meta:
        model = Stock
        fields = ['warehouse','product_id','quantity']

# class SaleOrderForm(forms.ModelForm):
#     class Meta:
#         model = SaleOrder
#         fields = ['customer','order_date','status']
#     #     widgets = {
#     #     'order_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control','placeholder':'Select a date', 'type':'date'}),
#     # }

    
#     def __init__(self,*args, **kwargs):
#         super(SaleOrderForm,self).__init__(*args, **kwargs)

#         for i in self.fields:
#             self.fields[i].widget.attrs.update({'class':'form-control'})
#         # self.fields['name'].widget.attrs['placeholder'] = "Enter Name"
#         # self.fields['slug'].widget.attrs['placeholder'] = "Fill Slugname"

#         self.fields['customer'].empty_label = "Select Customer"
#         # self.fields["order_date"].initial = datetime.date.today()
#         self.fields["order_date"] = forms.DateField(widget=DateInput(format=('%Y-%m-%d'),attrs={'class':'form-control'}), initial=datetime.date.today())
#         self.fields["customer"].queryset = Customer.objects.filter(is_customer=True)
        
        


# SaleOrderLineFormSet = modelformset_factory(SaleOrderLine,fields=('product','quantity',))

# # AuthorFormSet = modelformset_factory(Author, fields=('name', 'title'))

      
       