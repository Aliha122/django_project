from django.urls import path 
from .views import login_user , log_user  , show_blog , create_post , show_person_blog2  , CreateUserSuperUser 

app_name = "Profile"

urlpatterns = [
     path('login/' ,login_user , name="login" ) , 
     path('logout/' , log_user , name="logout" ) , 
     path('blogs/' , show_blog , name="show_blog" ) , 
     path('create_post/' , create_post  , name="create_post" ) , 
     path('blog_user/<int:id>/' , show_person_blog2 , name="show_person_blog2" ) , 
     path('add_user/' , CreateUserSuperUser , name="add_user"  ) , 
     
]
