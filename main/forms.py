from django import forms


class AddOrderForm(forms.Form):
    customer_no = forms.IntegerField(label='Customer no')
    customer_name = forms.CharField(label='Customer Name', max_length=50)
    date = forms.DateField(label='Date')
    base_recipe = forms.CharField(label='Base Recipe')
    add_on_qty = forms.IntegerField(label='Add-on Qty')
    add_on_name = forms.CharField(label='Add-on')

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