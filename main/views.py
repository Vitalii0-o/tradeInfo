from django.shortcuts import render
from django.http import JsonResponse
from main.static.main.py.data_request import Stock_SMA, Stock_EMA, Upper_levels, Low_levels, Last_Month
from django.core.cache import cache


def index(request):
    return render(request, 'main/index.html')


def stock_sma(request):
    cache.clear()
    stock_name = request.GET.get("name", None)
    Stock_SMA(stock_name)
    Stock_EMA(stock_name)
    Upper_levels(stock_name)
    Low_levels(stock_name)
    Last_Month(stock_name)
    return render(request, 'main/index.html')





