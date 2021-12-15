from django import forms
from django.forms import (ModelForm, 
    TextInput, Textarea, widgets)
from .models import *

class AddOrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'

class AddItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

class AddCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class AddIngredient(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'

class AddBaseFlavor(forms.ModelForm):
    class Meta:
        model = BaseFlavor
        fields = '__all__'



INGREDIENT_CATEGORIES = (
    (1,'nuts'),
    (2,'fruits'),
    (3,'chocolate'),
    (4,'baked'),
    (5,'mix-in'),
    (6,'base'),
    (7,'topping')

)

class AddInventoryForm(forms.Form):
    ingredient_id = forms.IntegerField(label='Ingredient No.')
    ingredient_name = forms.CharField(label='Ingredient Name')
    ingredient_category = forms.ChoiceField(choices = INGREDIENT_CATEGORIES, label ='Category')
    ingredient_quantity = forms.IntegerField(label='Quantity')
    ingredient_price = forms.IntegerField(label='Price per Serving')