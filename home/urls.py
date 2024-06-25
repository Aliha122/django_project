from django.urls import path
from .views import hello 



app_name = "home"


urlpatterns = [

    path('' , hello , name="hello" ) , 
    
    
]
