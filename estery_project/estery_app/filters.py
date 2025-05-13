import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class SaleFilter(django_filters.FilterSet):
    
    class Meta:
        model = Sale
        fields = '__all__'
        exclude = [ 'item_name','quantity','unit_price','customer_name','customer_contact','status','total_amount','date_of_sale']



class ExpenseFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_of_expense", lookup_expr='gte')
    end_date = DateFilter(field_name="date_of_expense", lookup_expr='lte')
    # amount = CharFilter(field_name="amount", lookup_expr='icontains')


    class Meta:
        model = Expense
        fields = '__all__'
        exclude = [ 'person_responsible', 'date_of_expense','image','amount']

class PurchaseFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_of_expense", lookup_expr='gte')
    end_date = DateFilter(field_name="date_of_expense", lookup_expr='lte')
    # amount = CharFilter(field_name="amount", lookup_expr='icontains')


    class Meta:
        model = Expense
        fields = '__all__'
        exclude = [ 'person_responsible', 'date_of_expense','image','amount']