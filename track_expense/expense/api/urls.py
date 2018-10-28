from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^expense/$',
	views.ExpenseListView.as_view(),
	name='expense_list'),
url(r'^expense/(?P<pk>\d+)/$',
	views.ExpenseDetailView.as_view(),
	name='expense_detail'),
]