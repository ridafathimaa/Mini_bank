from django.shortcuts import render, redirect
from .models import Register,Login
from django.http import HttpResponse

# Create your views here.
def display(request):
    return render(request,'register.html')
def register(request):
    if request.method == 'POST':
        account_no = request.POST['Account_no']
        name = request.POST['Name']
        phone_no = request.POST['Phone_no']
        balance = request.POST['Balance']
        username = request.POST['Username']
        password = request.POST['Password']
        data = Register.objects.create(account_no=account_no,name=name,phone_no=phone_no,balance=balance,username=username)
        data.save()
        data1 = Login.objects.create(username=username, password=password)
        data1.save()
        return HttpResponse("created")
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            data = Login.objects.get(username=username)
            if data.password == password:
                request.session['id'] = username  # session created
                return redirect(profile)
            else:
                return HttpResponse('password error')
        except Exception:
            return HttpResponse("username error")
    else:
        return render(request, 'login.html')

def profile(request):
    if 'id' in request.session:
        username = request.session['id']
        if request.method == 'GET':
            data = Register.objects.filter(username=username).all()
            return render(request, 'profile.html', {'data': data})

def logout(request):
    if 'id' in request.session:
        request.session.flush()
        return redirect(login)


def regtolog(request):
    return redirect(login)
def acctodep(request):
    return redirect(deposit)
def acctowit(request):
    return redirect(withdraw)
def deposit(request):
    return render(request,'deposite.html')
def withdraw(request):
    return render(request,'withdraw.html')
def add(request):
    if request.method=='POST':
        account_no=request.POST['Account_no']
        deposit=int(request.POST['Deposit'])
        data=Register.objects.get(account_no=account_no)
        data.balance+=deposit
        data.save()
        context = {
            'message': "the amount is deposit from your account"
        }
        return render(request,'deposite.html',context)
def take(request):
    if request.method=='POST':
        account_no=request.POST['Account_no']
        withdraw=int(request.POST['Withdraw'])
        if withdraw % 100==0 or withdraw % 200==0 or withdraw % 500==0:
         data=Register.objects.get(account_no=account_no)
         data.balance -=withdraw
         data.save()
         context = {
            'message': "the amount is withdraw from your account"
         }
        return render(request,'withdraw.html',context)

