from django.contrib import admin
from django.urls import path,include
from . import views
admin_url = "saAm"
super_admin_url = "SAam"

urlpatterns = [
    path('merchant-status/',views.merchant_status,name='merchant_status'),
    path('virtual-transaction/',views.virtual_transaction,name='virtual_transaction'),

]