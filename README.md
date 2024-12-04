# Ex02 Django ORM Web Application
## Date: 4.12.2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

![alt text](<Screenshot 2024-12-04 111121.png>)




## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py
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
admin.py
from django.contrib import admin
from .models import Bankloan,BankloanAdmin
admin.site.register(Bankloan,BankloanAdmin)
```


## OUTPUT

![alt text](<Screenshot 2024-12-04 105137.png>)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
