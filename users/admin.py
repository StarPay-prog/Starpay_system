from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email','is_staff','is_active')
    list_filter = ('email','is_staff','is_active')
    # readonly_fields = ('balance',)
    fieldsets = (
        (None,{'fields':('email','password')}),
        ('Permission',{'fields':('is_staff','is_active','is_Teacher','first_name','last_name','contact_no')}),
    )
    add_fieldsets = (
        (None,{'classes':('wide',),
               'fields':('email','password1','password2','is_staff','is_active','is_Teacher','first_name','last_name','contact_no')}),
        
    )
    search_fields = ('email',)
    ordering = ('email',)


   
admin.site.register(CustomUser,CustomUserAdmin),
admin.site.register(Transection),
admin.site.register(sale),
admin.site.register(Journal),

# admin.site.register(Transaction_Staff),