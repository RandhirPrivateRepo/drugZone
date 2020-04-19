from drugZoneUsers.models import *
from django import forms  

 
class CustomUserForm(forms.ModelForm):  
    class Meta:  
        model = CustomUser  
        fields = "__all__"  




class LoginModelForm(forms.ModelForm):

	email = forms.EmailField(
		widget=forms.EmailInput(
		attrs={
		"placeholder" : "Email",                
		"class": "form-control"
		}
	))
	password = forms.CharField(
		widget=forms.PasswordInput(
		attrs={
		"placeholder" : "Password",                
		"class": "form-control"
		}
	))  
	class Meta:  
		model = CustomUser  
		fields = ['email','password']
       
        