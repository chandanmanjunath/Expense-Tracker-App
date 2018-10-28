from rest_framework import generics
from ..models import Expense
from .serializers import ExpenseSerializer

#Below class is used for list view
class ExpenseListView(generics.ListAPIView):
	queryset = Expense.objects.all()
	serializer_class = ExpenseSerializer

#Below class is used for detail view
class ExpenseDetailView(generics.RetrieveAPIView):
	queryset = Expense.objects.all()
	serializer_class = ExpenseSerializer