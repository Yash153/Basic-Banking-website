
from django.contrib import admin
from django.urls import path
from bankingapp.views import home, createcustomer, viewcustomer, view, contact, transfer, transferhistory

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = 'home'),
    path('createcustomer/', createcustomer, name = 'createcustomer'),
    path('viewcustomer/', viewcustomer, name = "viewcustomer"),
    path('view/<int:id>', view, name = 'view'),
    path('contact/', contact, name = 'contact'),
    path('transfer/', transfer, name = 'transfer'),
    path('transferhistory/', transferhistory, name = 'transferhistory'),
]
