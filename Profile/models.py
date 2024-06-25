from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class AccountInformation(models.Model) : 
    
    ACCESS_LEVEL_STATUS = (
        ('R' , 'فقط خواندن') , 
        ('R_W' , 'خواندن و نوشتن') 
    )
    
    
    human = models.OneToOneField(User,verbose_name="فرد مورد نظر" , on_delete=models.CASCADE )
    phone = models.CharField(max_length=11 , verbose_name='تلفن' , blank=False ) 
    age   = models.PositiveIntegerField(verbose_name='سن کاربر' , null = True ) 
    access_level = models.CharField(verbose_name="مشخص کردن سطح دسترسی" , max_length=20 , choices=ACCESS_LEVEL_STATUS , default='R' )
    
    def __str__(self) -> str:
        return f"{self.human.username} - {self.phone} "
    
    class Meta : 
        db_table = 'AccountInformation'
        verbose_name_plural = 'حساب کاربری'
    
    
  
  
    
class blog(models.Model):
    
    
    STATUS_CHOICES = (
        ('draft' , 'پیش نویس') ,
        ('public' , 'منتشر شود')
        )
    

    
    title  = models.CharField(max_length=100, verbose_name="موضوع " )
    slug   = models.SlugField(verbose_name='آدرس اینترنتی این پست' , unique=False  ) 
    author = models.ForeignKey(AccountInformation , null = True  , on_delete=models.CASCADE , verbose_name="نویسنده" , )
    description = models.TextField(verbose_name="توضیحات این پست")
    status  = models.CharField(max_length= 10 , null = True  ,  verbose_name='وضعیت انتشار این پست' , choices=STATUS_CHOICES , default='draft' ) 
    
    
    def __str__(self) : 
        return self.title 
    
    
    class Meta : 
        db_table = "blog" 
        verbose_name_plural = 'پست ها '
