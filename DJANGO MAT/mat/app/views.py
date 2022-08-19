from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from app.models import Profile,Expense


# Create your views here.

def home(request):
    return render(request,'mainfile.html')

def mainpage(request):
    profile=Profile.objects.filter(user=request.user).first()
    expenses=Expense.objects.filter(user=request.user)
   
    if request.method=='POST':
        text=request.POST['text']
        amount=request.POST['amount']
        expense_type1=request.POST['expense_type']
        expense=Expense(name=text,expense_type=expense_type1,amount=amount,user=request.user)   
        expense.save()
        # profile.balance=0*profile.balance+profile.balance

        if expense_type1=='Positive':
            profile.balance+=float(amount)
            profile.income+=float(amount)
        else:
             profile.balance-=float(amount)
             profile.expense+=float(amount)

        profile.save()
        return redirect('mainpage')
    
    context={'profile': profile,'expenses':expenses}
    return render(request,'expnsinterface.html',context)


def delete(request,uid):
    expenses=Expense.objects.get(pk=uid)
    profile=Profile.objects.filter(user=request.user).first()
    
    amount=expenses.amount
    expense_type=expenses.expense_type
    if expense_type=='Positive':
         profile.balance-=float(amount)
         profile.income-=float(amount)
    else:
         profile.balance+=float(amount)
         profile.expense-=float(amount)
         
    expenses.delete()
    
    
    profile.save()
    return redirect('mainpage')



def login_user(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('mainpage')
        else:
            messages.success(request,"There was an error in logging in")
            return redirect('login')    
    
    return render(request,"login.html")

def logout_user(request):
    logout(request)
    messages.success(request,"user loged out successfully!")
    return redirect("login")

def signup(request):

    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.success(request,'username already exists')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,password=pass1,email=email)
                user.save();
                # user=authenticate(username=username,password=pass1)
                # login(request,user)
                profiles=Profile(user=user,balance=0,income=0,expense=0)
                messages.success(request,'user Successfully created')
                profiles.save()
                return redirect('login')
        else:
            messages.success(request,'passwords not matched')
            return redirect('signup')


    return render(request,"signupminpro.html")