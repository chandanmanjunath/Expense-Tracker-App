from django import forms
from django.contrib.auth.models import User
from .models import Profile,Expense

#Form for login
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

#Form for Registration
class UserRegistrationForm(forms.ModelForm):

        password = forms.CharField(label='Password',
                                   widget=forms.PasswordInput)
        password2 = forms.CharField(label='Repeat password',
                                    widget=forms.PasswordInput)
        #Class meta is used to specify any fields other than form fields
        class Meta:
                #use imported user model
                model = User
                #Include the below set of fields in form
                fields = ('username', 'first_name', 'email')
        #The below method is written to verify the two entered passwords
        def clean_password2(self):
            #get the form field data from cleaned_data dictionay to cd variable
            cd = self.cleaned_data
            #if first and second password are not sa,e raise validation error
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Passwords don\'t match.')
            #return the second password
            return cd['password2']
            
#Form for User Edit           
class UserEditForm(forms.ModelForm):
        class Meta:
            model = User
            fields = ('first_name', 'last_name', 'email')

#Form for Profile Edit                 
class ProfileEditForm(forms.ModelForm):
        class Meta:
            model = Profile
            fields = ('date_of_birth', 'photo')

#Form for Expense Creation            
class ExpenseCreateForm(forms.ModelForm):
        def __init__(self, *args, **kwargs):
             self.request = kwargs.pop('request', None)
             return super(ExpenseCreateForm, self).__init__(*args, **kwargs)
             
        def save(self, *args, **kwargs):
             kwargs['commit']=False
             obj = super(ExpenseCreateForm, self).save(*args, **kwargs)
             if self.request:
                obj.user = self.request.user
             obj.save()
             return obj
        class Meta:
            model = Expense
            fields = ('expense_name', 'expense_description','price','expense_image')
			#Labels used here to provide custom form field names
            labels = {'price': 'Price(In Rupees)','expense_name':'Expense Name','expense_description':'Expense Description','expense_image':'Expense Image'}

#Form for Expense Edit              
class ExpenseEditForm(forms.ModelForm):
        class Meta:
            model = Expense
            fields = ('expense_name', 'expense_description','price','expense_image')
			#Labels used here to provide custom form field names
            labels = {'price': 'Price(In Rupees)','expense_name':'Expense Name','expense_description':'Expense Description','expense_image':'Expense Image'}
            

