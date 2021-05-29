from django.shortcuts import render,redirect
from .models import Portfolio,Client,Stock
from .forms import CreateUserForm
from .decorators import unauthenticated_user,allowed_users
from basic_app.stock_data import candlestick_data,get_data

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User,Group
from django.contrib.auth.decorators import login_required
from basic_app.get_news import getNews
from basic_app.get_stock_info import getStockInfo
from django.http import JsonResponse
from json import dumps,loads


def dashboard(request):
    return render(request,"basic_app/dashboard.html")



@login_required(login_url='basic_app:login')
@allowed_users(allowed_roles=['Client'])
def index(request):
    if request.is_ajax():
        res = None
        data = request.POST.get('searchData')
        item = getStockInfo(data)
        if len(item)>0 and len(data):
            res = item
        else:
            res = 'No stocks found..'

        #print(data)

        return JsonResponse({'data':res})

    user = request.user
    client = Client.objects.get(user=user)
    portfolio = Portfolio.objects.get(client=client)
    stocks = portfolio.stocks.all()
    #print(stocks)
    #print(stocks)
    news = getNews("business")
    #print(news)
    context = {'stocks':stocks,'news':news}

    return render(request,"basic_app/index.html",context)

@login_required(login_url='basic_app:login')
@allowed_users(allowed_roles=['Client'])
def profile(request):
    client = request.user
    return render(request,"basic_app/profile.html",{'client':client})

@login_required(login_url='basic_app:login')
@allowed_users(allowed_roles=['Client'])
def portfolio(request):
    user = request.user
    client = Client.objects.get(user=user)
    portfolio = Portfolio.objects.get(client=client)
    stocks = portfolio.stocks.all()
    context = {'stocks':stocks}
    return render(request,"basic_app/portfolio.html",context)

@login_required(login_url='basic_app:login')
def stock(request,symbol):
    data = candlestick_data(symbol)
    item = getStockInfo(symbol)
    info = get_data(symbol)

    context ={'data':dumps(data),'item':dumps(item),'info':info}   #"price_prediction":price_prediction


    return render(request,"basic_app/stock.html",context)

@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username =username, password=password)

        if user is not None:
            login(request,user)
            if(user.groups.all()[0].name == 'Admin'):
                return redirect("basic_app:stats")
            else:
                return redirect("basic_app:index")
        else:
            messages.info(request,"Incorrect username or password")
            return redirect("basic_app:login")


    return render(request,"basic_app/login.html")

@login_required(login_url='basic_app:login')
def logoutUser(request):
    logout(request)
    return redirect("basic_app:login")

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Client')
            user.groups.add(group)
            client = Client.objects.create(user=user)
            portfolio = Portfolio.objects.create(client=client)
            return redirect('basic_app:login')

    context = {'form':form}
    return render(request,"basic_app/register.html",context)

@login_required(login_url='basic_app:login')
@allowed_users(allowed_roles=['Admin'])
def statisticsAdmin(request):
    return render(request,"basic_app/statisticsAdmin.html")



# def search_results(request):
#     if request.is_ajax():
#         data = request.POST.get('searchData')
#         return JsonResponse({'data':data})
#     return JsonResponse({})



# Underdog Stocks(already listed)
# Indian Stocks (you cant go wrong)(fundamentally strong indian companies)
# Upcoming IPOs
# Price Prediction
# Patience
# Company risk
# Most Popular (Stocks,Brokers)
# Information Section(keep learning)
