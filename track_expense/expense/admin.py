from django.contrib import admin

# Register your models here.

from .models import Expense

#add the created model to admin site	
admin.site.register(Expense)
