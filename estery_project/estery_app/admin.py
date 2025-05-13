from django.contrib import admin
from .models import *

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
	list_display = ("emp_id","full_name","telephone","date_of_birth","home_address",)



@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
	list_display = ("person_responsible","purpose","amount","date_of_expense","branch",)

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
	list_display = ("person_responsible","item_name","quantity","amount","date_of_purchase","branch","supplier_name","supplier_contact",)

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
	list_display = ("person_responsible","item_name","unit_price","quantity","total_amount","date_of_sale","branch",)