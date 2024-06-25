from django.db import models
from django_jalali.db import models as jmodels
# Create your models here.


class person(models.Model):
    name=models.CharField(max_length = 100 , verbose_name="نام" )
    family = models.CharField(max_length=100  , verbose_name="فامیلی") 
    email  = models.CharField(null= True,verbose_name="ایمیل")
    hb     = jmodels.jDateTimeField(null = True )
    
    
    def __str__(self) :
        return f"{self.name} - {self.family} "
    
    
    class Meta : 
        verbose_name_plural = "معلم"
    
    
    
    
class Student(models.Model) : 
    name = models.CharField(max_length=100 , verbose_name='نام دانش آموز')
    familly = models.CharField(max_length=100 , verbose_name='نام  خانوادگی دانش آموز')

    def __str__(self) : 
        return f"{self.name} - {self.familly}"
    
    class Meta : 
        verbose_name_plural = "دانش آموز"
 
class Course(models.Model):
     
    name    = models.CharField(max_length=100 , verbose_name='نام درس')
    teacher = models.OneToOneField(person  , on_delete = models.SET_NULL , null = True  , verbose_name='معلم' )
    student = models.ForeignKey(Student  , related_name='student' , on_delete = models.SET_NULL , null = True  , verbose_name='دانش آموز' )
     
     
     
    def  __str__(self) -> str:
         return f"{self.name} - {self.teacher} - {self.student} "
     
     
     
     
    class Meta : 
        verbose_name_plural ="درس"