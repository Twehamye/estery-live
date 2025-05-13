from django.contrib.auth.models import User
from django import forms
from .models import Employee,Expense,Sale,Purchase,Stock,ImageModel,Sales
from django.forms import ModelForm, widgets, DateTimeField, DateField, DateInput
from bootstrap_datepicker_plus.widgets import DatePickerInput


class EmployeeForm(ModelForm):
    date_of_birth= forms.DateField(widget=forms.widgets.DateInput(
        attrs={'type': 'date'}))
    class Meta:
        model = Employee
        fields = '__all__'


class ExpenseForm(ModelForm):
    date_of_expense = forms.DateField(widget=forms.widgets.DateInput(
        attrs={'type': 'date'})
    )
    class Meta:
        model = Expense
        fields = '__all__'

class PurchaseForm(ModelForm):
    date_of_purchase = forms.DateField(widget=forms.widgets.DateInput(
        attrs={'type': 'date'})
    )
    class Meta:
        model = Purchase
        fields = '__all__'

class SaleForm(ModelForm):
    date_of_sale = forms.DateField(widget=forms.widgets.DateInput(
        attrs={'type': 'date'})
    )
    class Meta:
        model = Sale
        fields = '__all__'

class StockForm(forms.ModelForm):
    date = forms.DateField(widget=forms.widgets.DateInput(
        attrs={'type': 'date'})
    )
    class Meta:
        model = Stock
        fields = '__all__'
        exclude = [ 'cost_price', 'selling_price']

class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = '__all__'

class SalesForm(forms.ModelForm):
    date = forms.DateField(widget=forms.widgets.DateInput(
        attrs={'type': 'date'})
    )
    class Meta:
        model = Sales
        fields = '__all__'