from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout 
from .models import AccountInformation , blog 
from .forms import Formlog , BlogForm , AddUserForm 
from django.contrib import messages 
from django.contrib.auth.models import User 
# Create your views here.



def login_user(request) : 
    
    if request.method == "POST" :
        form  = Formlog(request.POST) 
        if form.is_valid() :
            new_username =  form.cleaned_data['username']
            new_password =  form.cleaned_data['passwrd']
            
            user = authenticate(request , username = new_username , password = new_password ) 
            if user is not None :
                login(request , user )
                
                messages.success(request , 'با موفقیت وارد شدید' , 'success')
                return redirect('home:hello')
                
                
        else : 
            messages.error(request , 'با موفقیت وارد نشدید' , 'error')
            return redirect('home:hello')
            
    else : 
        return render(request , 'log.html' , {} )
        
def log_user(request) : 
    
    logout(request)
    return redirect('home:hello')
                              
def show_blog(request) : 
    total_data = blog.objects.filter(status = 'public' ) 
    
    return render(request , 'show_blog.html' , {'data' : total_data })
    
def show_person_blog2(request , id ) : 
    t = blog.objects.filter(author__human__id = id )
    
    return render(request , 'show_person_blog.html' , {'blog' : t })
    
def create_post(request) : 
    
    if request.method == "POST" : 
        form = BlogForm(request.POST)
        if form.is_valid() : 
            new_title = form.cleaned_data['title']
            new_description = form.cleaned_data['description']
            print( "************************************************** / " , form.cleaned_data['status_check'])
            
            
            if request.user.is_authenticated : 
                new_person = AccountInformation.objects.get(human__username = request.user.username ) 
            
                b1 = blog(title = new_title , description = new_description , author = new_person , status = form.cleaned_data['status_check'] )
                b1.save() 
                messages.success(request , 'پست با موفقیت ذخیره شد' , 'success')    
                return redirect('home:hello')
                
                
    return render(request , 'form_blog_created.html' , {})
            

def CreateUserSuperUser(request) : 
    
    if request.user.is_authenticated : 
        user = request.user 
        if user.is_superuser :
            if request.method == "POST" :  
                form = AddUserForm(request.POST) 
                if form.is_valid() : 
                    new_username = form.cleaned_data['username']
                    new_email    = form.changed_data['user_email'] 
                    new_password = form.changed_data['password']
                    
                    check_user = User.objects.filter(username = new_username ).exists() 
                    if check_user == False   :
                        new_user_created = User.objects.create_user(username = new_username , email = new_email , password=new_password    )
                        new_account = AccountInformation(human = new_user_created , phone = "--" , age = 0 , access_level = 'R' ) 
                        new_account.save() 
                        messages.success(request , 'با موفقیت حساب کاربری ساخته شد ' , 'success' )
                        
                    
                    
                    
    else : 
        messages.error(request , 'شما باید ابتدا وارد حساب کاربری خود شوید' , 'error')
        return redirect('Profile:login') 
    
    return render(request , 'add_user.html' , {})            
            
            
    
    
    
    
    
            
            
    
    



