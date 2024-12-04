from django.db import models
from django.contrib import admin
class Bankloan (models.Model):
    Customer_id=models.IntegerField(primary_key=True)
    Customer_name=models.CharField(max_length=100)
    Account_type=models.CharField(max_length=50)
    Account_number=models.IntegerField()
    Age=models.IntegerField()
    Loan_type=models.CharField(max_length=30)
    Loan_amount=models.IntegerField()
 
class BankloanAdmin(admin.ModelAdmin):
    list_display=('Customer_id','Customer_name','Account_type','Account_number','Age','Loan_type','Loan_amount')