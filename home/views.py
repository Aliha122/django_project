from django.shortcuts import render
from .models import person , Course , Student 
from Profile.models import AccountInformation 
# Create your views here.




def hello(request) : 
    
    data_person  = person.objects.all()
    data_course  = Course.objects.all()
    data_student = Student.objects.all()

    global logperson
    logperson = None 

    if request.user.is_authenticated : 
        
        logperson = AccountInformation.objects.get(human = request.user )
    
    content = {'person' : data_person , 'course' : data_course , 'student' :data_student , 'key_logperson' : logperson  }
    return render(request , 'first_page.html' , content )
    
     
    