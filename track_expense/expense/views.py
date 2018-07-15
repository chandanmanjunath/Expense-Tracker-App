from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.contrib.auth import authenticate, login
#import all the necessary forms
from .forms import LoginForm,UserRegistrationForm,UserEditForm,ProfileEditForm,ExpenseCreateForm,ExpenseEditForm

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import Profile,Expense


#Import the messages from django.contrib
from django.contrib import messages
from django.db.models import Sum

@login_required
def dashboard(request):
    return render(request,
                'expense/dashboard.html',
                {'section': 'dashboard'})

#Method(view) for handling user login
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated '\
                                        'successfully')
                else:
                    return HttpResponse('Disabled account')
    else:
        form = LoginForm()
        return render(request, 'expense/login.html', {'form': form})


#Method(view) to handle user registration 
def register(request):
        #identify post method
        if request.method == 'POST':
            #get the instance of submitted form
            user_form = UserRegistrationForm(request.POST)
            #if form is valid
            if user_form.is_valid():
                    # Create a new user object but avoid saving it yet
                    new_user = user_form.save(commit=False)
                    # Set the chosen password,set_password method encryptes the password
                    new_user.set_password(user_form.cleaned_data['password'])
                    # Save the User object after the encrypted password
                    new_user.save()
                    profile = Profile.objects.create(user=new_user)
                    return render(request,
                                'expense/register_done.html',
                                {'new_user': new_user})
            
        else:
                user_form = UserRegistrationForm()
                return render(request,
                        'expense/register.html',
                        {'user_form': user_form})
                        
                        
@login_required
def edit(request):
        if request.method == 'POST':
                #create a user_form object
                #Use request.user instance
                #data use request.Post data
                user_form = UserEditForm(instance=request.user,
                                        data=request.POST)
                #create a profile_form object
                #use request.user.profile instance
                #The user object is referenced from  model class
                #The profile object is referenced from register method above
                profile_form = ProfileEditForm(instance=request.user.profile,
                                                data=request.POST,
                                               files=request.FILES)
                #Check if both user_form and profile_form is valid
                if user_form.is_valid() and profile_form.is_valid():
                        #save respective details to database
                        user_form.save()
                        profile_form.save()
                        messages.success(request, 'Profile updated successfully')
                else :
                        #Use the messages framework to display error  if form and profile are not valid
                        messages.error(request, 'Error updating your profile')
        #else load the original form instance
        else:
                user_form = UserEditForm(instance=request.user)
                profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request,
                    'expense/edit.html',
                    {'user_form': user_form,
                    'profile_form': profile_form})

#Method(view) to handle expense addition
@login_required                   
def expense_add(request):
        #identify post method
        if request.method == 'POST':
            #get the instance of submitted form
            expense_form = ExpenseCreateForm(request.POST,files=request.FILES)
            #if form is valid
            if expense_form.is_valid():
                    # Save the User object after the request user is assigned
                    bet = expense_form.save(commit=False)
                    bet.user_tar = request.user
                    bet.save()
                    #expense_form.save()
                    return render(request,
                                'expense/expense_form_saved.html',
                                {'expense_form': expense_form})
            
        else:
                expense_form = ExpenseCreateForm()
                return render(request,
                        'expense/expense_create.html',
                        {'expense_form': expense_form})
                        
#Method(view) to handle expense list display 
@login_required                       
def expense_list(request):
        #Filter the expenses for the logged in user
        expense=Expense.objects.filter(user_tar_id=request.user)
        #Calculate the sum of expenses for the logged in user
        expense_sum=Expense.objects.filter(user_tar_id=request.user).aggregate(Sum('price'))
                                  
        return render(request,
                'expense/expense_list.html',
                {'expense': expense,'expense_sum': expense_sum})
        
        
#Method(view) to handle expense edit      
@login_required
def expense_edit(request, id = None):
        #Get the Id of expense to be edited
        if id:
            expense_new = Expense.objects.get(pk = id)
            print(expense_new.expense_name)
        else :
            expense_new = None
        if request.method == 'POST':
                        #If the form is submitted ,check if valid,then save
                        form = ExpenseEditForm(data=request.POST,files=request.FILES, instance=expense_new)
                        #print(expense_new.id)
                        if form.is_valid():
                            form.save()
                            return render(request,'expense/expense_edit_done.html',{'form': form})   
        else:
                        #Display the form instance requested for GET request
                        form = ExpenseEditForm(instance = expense_new)
        return render(request,'expense/expense_edit.html',{'form': form})
        
#Method(view) to handle expense Delete       
@login_required     
def expense_delete(request,id= None):
       #Get the Id of expense to be deleted and delete it
       if id:
            instance = Expense.objects.get(id=id)
            instance.delete()
       #return the instance to display in template
       return render(request,
                'expense/delete_expense.html',
                {'instance': instance})
