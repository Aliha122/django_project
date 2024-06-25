from django import forms

class Formlog(forms.Form):
    
    username = forms.CharField()
    passwrd  = forms.CharField()
    
    
    
class BlogForm(forms.Form) : 
    
    title = forms.CharField()
    description  = forms.CharField(widget=forms.Textarea )
    status_check = forms.CharField() 
    
class AddUserForm(forms.Form) : 
    
    username   = forms.CharField(widget=forms.TextInput )
    user_email = forms.EmailField(widget=forms.EmailInput)
    password   = forms.CharField(widget=forms.PasswordInput)
    
    
    
    
