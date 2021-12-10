from django import forms


class AddOrderForm(forms.Form):
    customer_no = forms.IntegerField(label='Customer no')
    customer_name = forms.CharField(label='Customer Name', max_length=50)
    date = forms.DateField(label='Date')
    base_recipe = forms.CharField(label='Base Recipe')
    add_on_qty = forms.IntegerField(label='Add-on Qty')
    add_on_name = forms.CharField(label='Add-on')