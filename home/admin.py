from django.contrib import admin
from .models import person , Student , Course 

# Register your models here.



@admin.register(Student)
class Student_Admin(admin.ModelAdmin) : 
    list_display = ('name' , 'familly' )
    

@admin.register(Course)
class Course_Admin(admin.ModelAdmin) : 
    list_display = ('name' , 'teacher' , 'student'  , "custom_display" )
    
    
    def custom_display(self , obj ) : 
        s = f"{obj.teacher.name} - {obj.student.name}"
        return s  
    
    
    custom_display.short_description = 'نام استاد + نان دانش آموز'
    


@admin.register(person)
class person_admin(admin.ModelAdmin) : 
    list_display = ('name' , 'family' ) 
    