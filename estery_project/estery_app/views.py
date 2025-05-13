from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Employee,Sale,Expense,Purchase,Stock, ImageModel,Sales
from .models import *
from django.contrib.auth import authenticate, login, logout
from .forms import EmployeeForm,SaleForm,ExpenseForm,PurchaseForm,StockForm,SalesForm,ImageForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.db.models import Q
from django.db.models import Sum, Avg, Count,F
from django.views.generic import ListView
from .filters import PurchaseFilter,ExpenseFilter,SaleFilter
from django.db import connection
from django.db.models.expressions import RawSQL
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import csv
from django.db.models.functions import TruncDate


def index(request):
    return render(request, 'index.html')

def index_admin(request):
    return render(request, 'index_admin.html')

def about(request):
    return render(request, 'about.html')

def product(request):
    return render(request, 'product.html')

def contact(request):
    return render(request, 'contact.html')

@login_required(login_url='login')
def home(request):
    total_employees = Employee.objects.all().count() #aggregate(Count('member_id'))
    # pending_deposits = Deposit.objects.filter(status='pending').count()
    # approved_deposits = Deposit.objects.filter(status='Approved').count()
    # deposits = Deposit.objects.all().order_by("-date_created") 
    # myFilter = DepositFilter(request.GET, queryset=deposits)
    # deposits = myFilter.qs
    expenses_total = Expense.objects.all().aggregate(models.Sum('amount'))['amount__sum'] or 0 
    # savings_total = Deposit.objects.filter(status='approved').aggregate(models.Sum('total_amount'))['total_amount__sum'] or 0 
    # savings_total = Deposit.objects.filter(status='approved').aggregate(models.Sum('amount_cash'))['amount_cash__sum'] or 0 
    # savings_total = Deposit.objects.filter(status='approved').aggregate(models.Sum('amount_cash'))['amount_cash__sum'] or 0 
    # otherincome = OtherIncome.objects.aggregate(models.Sum('amount'))['amount__sum'] or 0

    # current_balance = savings_total + otherincome - expenses_total 

    # grand_total = savings_total + expenses_total + otherincome

    context = {
        # 'pending_deposits': pending_deposits,
        # 'approved_deposits': approved_deposits,
        'total_employees': total_employees, 
        # # 'total_savings': total_savings,
        # 'deposits': deposits,
        # 'myFilter': myFilter, 
        # 'current_balance': current_balance,
        # 'savings_total': savings_total,
        # 'expenses_total':expenses_total,
        # 'grand_total': grand_total,
        
        # 'otherincome':otherincome,
        
      }

    return render(request,'dashboard.html', context)
    

def index(request):
    context = {
        'variable1': 'Hello',
        'variable2': 'World',
    }
    return render(request, 'index.html', context)

    
class ImageListView(ListView):
    model = ImageModel
    template_name = 'image_list.html'
    context_object_name = 'images'

def employee(request, emp_id):
    employee = Employee.objects.get(emp_id=emp_id)
    # deposits = employee.deposit_set.all().order_by('-date_created')
    expenses = employee.expense_set.all().order_by('-date_of_expense')
    purchases = employee.purchase_set.all().order_by('-date_of_purchase')
    # used_total = employee.deposit_set.filter(status='Approved').aggregate(models.Sum('amount_used'))['amount_used__sum'] or 0
    # cash_total = employee.deposit_set.filter(status='Approved').aggregate(models.Sum('amount_cash'))['amount_cash__sum'] or 0
    # ind_fine = member.fine_set.filter(status='unpaid').aggregate(models.Sum('amount'))['amount__sum'] or 0
    # myFilter = DepositFilter(request.GET, queryset=deposits)
    # deposits = myFilter.qs
    
    context = {
                'employee': employee, 
                # 'deposits': deposits, 
                'purchases':purchases,
                'expenses':expenses,
                # 'used_total':used_total,
                # 'myFilter': myFilter,
                # 'cash_total': cash_total,
    }

    return render(request, 'emp_report.html', context)

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index_admin")
        else: 
            messages.info(request, "Username or password is incorrect")

    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('/')

def createEmployee(request):
    form = EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {'form': form}
    return render(request, 'employee_form.html', context)

def updateEmployee(request, emp_id):

    employee = Employee.objects.get(emp_id=emp_id)
    form = EmployeeForm(instance=employee)

    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'employee_form.html', context) 
    

def deleteEmployee(request, emp_id):
    employee = Employee.objects.get(emp_id=emp_id)
    if request.method == "POST":
        employee.delete()
        return redirect('home')

    context = {'item': employee } 

    return render(request, 'delete_employee.html', context) 

def allEmployee(request):

    employee_list = Employee.objects.all()  
         

    context = {
                'employee_list': employee_list, 
                    
        }  

    return render(request, 'all_employee.html', context )


def create_sale(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SaleForm()
    return render(request, 'create_sale.html', {'form': form})


def updateSale(request, id):
    sale = Sale.objects.get(id=id)
    form = SaleForm(instance=sale)

    if request.method == "POST":
        form = SaleForm(request.POST, instance=sale)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form } 

    return render(request, 'create_sale.html', context)         

def deleteSale(request, id):
    sale = Sale.objects.get(id=id)
    if request.method == "POST":
        sale.delete()
        return redirect('/')

    context = {'item': sale } 

    return render(request, 'delete_sale.html', context)

def allSale(request):
    search_sale = request.GET.get('search')
    if search_sale:

        sales = Sale.objects.filter(Q(amount__icontains=search_sale) |
                             Q(purpose__icontains=search_sale) |
                             Q(date_created__icontains=search_sale))
    else:
        # If not searched, return default members
        sales = Sale.objects.all().order_by("-date_of_sale") 
        myFilter = SaleFilter(request.GET, queryset=sales)
        sales = myFilter.qs   
         
        context = {'sales': sales,
                    'myFilter': myFilter
        } #'members': members} 

    return render(request, 'all_sale.html', context )



def createExpense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ExpenseForm()
    return render(request, 'create_expense.html', {'form': form})


def updateExpense(request, id):
    expense = Expense.objects.get(id=id)
    form = ExpenseForm(instance=expense)

    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form } 

    return render(request, 'create_expense.html', context)         

def deleteExpense(request, id):
    expense = Expense.objects.get(id=id)
    if request.method == "POST":
        expense.delete()
        return redirect('home')

    context = {'expense': expense } 

    return render(request, 'delete_expense.html', context) 

def allExpense(request):
    search_expense = request.GET.get('search')
    if search_expense:
        expenses = Expense.objects.filter(
                             Q(purpose__icontains=search_expense) |
                             Q(date_created__icontains=search_expense))
    else:
        # If not searched, return default members
        expenses = Expense.objects.all().order_by("-date_of_expense") 
        myFilter = ExpenseFilter(request.GET, queryset=expenses)
        expenses = myFilter.qs   
         
        context = {
                    'expenses': expenses,
                    'myFilter': myFilter
                    }
    return render(request, 'all_expenses.html', context )


def createPurchase(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PurchaseForm()
    return render(request, 'create_purchase.html', {'form': form})


def updatePurchase(request, id):
    purchase = Purchase.objects.get(id=id)
    form = PurchaseForm(instance=purchase)

    if request.method == "POST":
        form = PurchaseForm(request.POST, instance=purchase)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form } 

    return render(request, 'create_purchase.html', context)         

def deletePurchase(request, id):
    purchase = Purchase.objects.get(id=id)
    if request.method == "POST":
        purchase.delete()
        return redirect('/')

    context = {'purchase': purchase } 

    return render(request, 'delete_purchase.html', context)   

def allPurchase(request):

    purchase_list = Purchase.objects.all()  
         

    context = {
                'purchase_list': purchase_list, 
                    
        }  

    return render(request, 'all_purchases.html', context )

@login_required
def daily_report(request):
    # employee = Employee.objects.get()
    transactions = Sale.objects.filter().values('date_of_sale').annotate(Total_Sales=Sum(F('unit_price') * F('quantity'))).order_by('-date_of_sale')
    # sales = sale.deposit_set.all().order_by('-date_created')
    sales = Sale.objects.all().order_by('-date_of_sale')
    expenses = Expense.objects.all().order_by('-date_of_expense')
    purchases = Purchase.objects.all().order_by('-date_of_purchase')
    # total_sales = Sale.objects.all().aggregate(models.Sum('total_amount'))['total_amount__sum'] or 0
    total_sales = sum(obj.total_amount for obj in sales)
    total_purchases = Purchase.objects.all().aggregate(models.Sum('amount'))['amount__sum'] or 0
    total_expenses = Expense.objects.all().aggregate(models.Sum('amount'))['amount__sum'] or 0
    current_balance = total_sales - total_purchases - total_expenses 
    
    context = {
            'total_sales':total_sales,
            'total_purchases': total_purchases,
            'total_expenses' : total_expenses,
            'current_balance': current_balance,
            'transactions': transactions,
                
    }

    return render(request, 'daily_report.html', context)


@login_required 
def add_product(request):
    form=StockForm() 
    if request.method == 'POST': 
        form = StockForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('/') 
        else: 
            form = StockForm() 
    return render(request, 'add_product.html', {'form': form})



def image_upload_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = ImageForm()
    return render(request, 'image_upload.html', {'form': form})

def stock_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('stock_list')
    else:
        form = ImageForm()
    return render(request, 'stock_upload.html', {'form': form})


class ImageListView(ListView):
    model = ImageModel
    template_name = 'product.html'
    context_object_name = 'images'

class StockListView(ListView):
    model = ImageModel
    template_name = 'stocklist.html'
    context_object_name = 'images'

def edit_image(request, pk):
    image = Sales.objects.get(pk=pk)
    if request.method == 'POST':
        form = SalesForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('all_sales')
    else:
        form = SalesForm(instance=image)
    return render(request, 'edit_image.html', {'form': form})


def delete_image(request, pk):
    image = ImageModel.objects.get(pk=pk)
    if request.method == 'POST':
        image.delete()
        return redirect('image_list')
    return render(request, 'confirm_delete.html', {'image': image})

def sales_view(request):
    if request.method == 'POST':
        form = SalesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SalesForm()
    return render(request, 'sales.html', {'form': form})

class SalesListView(ListView):
    model = Sales
    template_name = 'all_sales.html'
    context_object_name = 'images'

def total_sales(request):
    # total_amount = Sales.objects.aggregate(Sum('item_total'))['amount__sum']
    queryset = Sales.objects.all()
    total_amount = Sales.objects.annotate(calculated_value=F('amount') * F('quantity')).aggregate(total=Sum('calculated_value'))['total']
    daily_sales = Sales.objects.all().order_by('-date')
    return render(request, 'total_sales.html', {'total_amount': total_amount, 'daily_sales': daily_sales})