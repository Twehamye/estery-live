from django.db import models
import datetime
from datetime import date  
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

class Employee(models.Model):
    sex_choices = (("Male","male"), ("Female","Female"))
    emp_id =models.CharField(max_length=10, primary_key=True )
    full_name = models.CharField(max_length=200, null=False)
    sex = models.CharField(max_length=10,choices = sex_choices)
    telephone = models.PositiveIntegerField()
    date_of_birth = models.DateField(validators=[MaxValueValidator(datetime.date.today)])
    parent_name = models.CharField(max_length=200, null=False)
    parent_telephone = models.PositiveIntegerField()
    home_address = models.CharField(max_length=300) 
    Registered_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):

        return self.emp_id + " " +self.full_name

class Expense(models.Model):
    branch_choices =(("Kalerwe","Kalerwe"),("kireka","kireka"))

    purpose = models.CharField(max_length=300, null=False)
    amount = models.PositiveIntegerField()
    date_of_expense = models.DateField()
    branch = models.CharField(max_length=200, null=False, choices = branch_choices)
    person_responsible = models.ForeignKey(Employee, on_delete=models.SET_DEFAULT, default=None, null=False)
    image = models.ImageField(upload_to='expenses/%Y/%m/%d',blank=True)

    def __str__(self):
        return self.purpose +"  "+ str(self.amount)


class Purchase(models.Model):
    branch_choices =(("Kalerwe","Kalerwe"),("kireka","kireka"))

    item_name = models.CharField(max_length=300, null=False)
    quantity = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    date_of_purchase = models.DateField()
    branch = models.CharField(max_length=30, null=False, choices = branch_choices)
    receipt_no = models.CharField(max_length=300)
    person_responsible = models.ForeignKey(Employee, on_delete=models.SET_DEFAULT, default=None, null=False)
    supplier_name = models.CharField(max_length=300, null=False)
    supplier_contact = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/%Y/%m/%d',blank=True)


class Sale(models.Model):
    branch_choices =(("Kalerwe","Kalerwe"),("kireka","kireka"))

    item_name = models.CharField(max_length=300, null=False)
    quantity = models.PositiveIntegerField()
    unit_price = models.PositiveIntegerField()
    date_of_sale = models.DateField()
    branch = models.CharField(max_length=30, null=False, choices = branch_choices)
    # receipt_no = models.CharField(max_length=300)
    person_responsible = models.ForeignKey(Employee, on_delete=models.SET_DEFAULT, default=None, null=False)
    customer_name = models.CharField(max_length=300, null=False)
    customer_contact = models.PositiveIntegerField()
    # receipt = models.ImageField(upload_to='deposits/%Y/%m/%d',blank=True)
    status = models.CharField(max_length=300)

    @property
    def total_amount(self):
    	total_amount = self.unit_price * self.quantity
    	return total_amount
    
class Stock(models.Model):
    date = models.DateField()
    item = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=10, decimal_places=1)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    supplier_name = models.CharField(max_length=255)
    supplier_number = models.IntegerField()
    image = models.ImageField(upload_to='images/')

class Sales(models.Model):
    date = models.DateField()
    item = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=10, decimal_places=1)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    cust_name = models.CharField(max_length=255)
    cust_number = models.IntegerField()
    image = models.ImageField(upload_to='images/')

    def item_total(self): 
        return self.quantity * self.amount 

class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255)
    description = models.TextField()
    tags = models.CharField(max_length=255)