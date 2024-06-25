from django.contrib import admin
from .models import AccountInformation ,blog

# Register your models here.


@admin.register(AccountInformation)
class AccountInformation_admin(admin.ModelAdmin) : 
    list_display = ('show_username' , 'phone'  , 'show_email'  ) 
    
  
    def show_username(self , obj  ) : 
        return obj.human.username 
    
    show_username.short_description = 'نام کاربری'
    
    def show_email(self , obj  ) : 
        return obj.human.email 
    
    show_email.short_description = "ایمیل کاربر"



@admin.register(blog)
class blog_admin(admin.ModelAdmin) : 
    list_display = ('title' , 'author' , 'status' , 'description','slug') 
    
    list_editable = ('status' , )
    prepopulated_fields = {'slug' : ('title' , )}
    
  