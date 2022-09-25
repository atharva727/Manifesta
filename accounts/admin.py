from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import User

class AccountAdmin (UserAdmin):
    list_display = ( 'username','email','is_vendor','id')
    search_fields =('email', 'username')
    readonly_fields= ('id', 'date_joined', 'last_login','is_vendor')
    
    filter_horizontal = ()
    list_filter = ('is_vendor','date_joined',)  
    fieldsets=()    
    ordering = ('id','username')

# Register your models here.
admin.site.register(User, AccountAdmin)