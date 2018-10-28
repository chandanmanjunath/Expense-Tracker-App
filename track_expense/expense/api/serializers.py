from rest_framework import serializers
from ..models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Expense
		#Set of below fields to be used in API
		fields = ('id','user_tar', 'expense_name', 'expense_description','price','expense_image','created')