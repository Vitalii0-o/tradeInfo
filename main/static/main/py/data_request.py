import yfinance as yf
import investpy
import pandas as pd
from datetime import date
import datetime as dt
import matplotlib.pyplot as plt


def Stock_SMA(stock_name):
    plt.style.use('fivethirtyeight')  # специальное отображение графиков для pyplot
    stock = stock_name
    country = 'ukraine'
    current_date = str(date.today().day) + '/' + str(date.today().month) + '/' + str(date.today().year)
    try:
        df = investpy.get_stock_historical_data(stock=stock, country=country, from_date='01/01/2021',
                                                to_date=current_date)
    except:
        df = yf.download(stock, start='2021-01-01', end=date.today(), progress=False)
    # Count SMA30 / SMA90
    SMA30 = pd.DataFrame()
    SMA30['Close Price'] = df['Close'].rolling(window=30).mean()
    SMA90 = pd.DataFrame()
    SMA90['Close Price'] = df['Close'].rolling(window=90).mean()
    data = pd.DataFrame()
    data['Stock'] = df['Close']
    data['SMA30'] = SMA30['Close Price']
    data['SMA90'] = SMA90['Close Price']

    # Визуализируем
    plt.figure(figsize=(12.6, 4.6))
    plt.plot(data['Stock'], label=stock, alpha=0.35)
    plt.plot(SMA30['Close Price'], label='SMA30', alpha=0.35)
    plt.plot(SMA90['Close Price'], label='SMA90', alpha=0.35)
    plt.title(stock + ' history (SMA)')
    plt.xlabel('01/01/2021 - ' + current_date)
    plt.ylabel('Close price')
    plt.legend(loc='upper left')
    plt.savefig('C:/Users/vital/PycharmProjects/tradeInfo/main/static/main/py/my_chart.png')


def Stock_EMA(stock_name):
    ''' stock - stock exchange abbreviation; country - the name of the country'''
    # Read data
    stock = stock_name
    country = 'ukraine'
    current_date = str(date.today().day) + '/' + str(date.today().month) + '/' + str(date.today().year)
    try:
        df = investpy.get_stock_historical_data(stock=stock, country=country, from_date='01/01/2019',
                                                to_date=current_date)
    except:
        df = yf.download(stock, start='2019-01-01', end=date.today(), progress=False)
    # Count EMA20 / EMA60
    EMA20 = pd.DataFrame()
    EMA20['Close Price'] = df['Close'].ewm(span=20).mean()
    EMA60 = pd.DataFrame()
    EMA60['Close Price'] = df['Close'].ewm(span=60).mean()
    data = pd.DataFrame()
    data['Stock'] = df['Close']
    data['EMA20'] = EMA20['Close Price']
    data['EMA60'] = EMA60['Close Price']

    # Визуализируем
    plt.figure(figsize=(12.6, 4.6))
    plt.plot(data['Stock'], label=stock, alpha=0.35)
    plt.plot(EMA20['Close Price'], label='EMA30', alpha=0.35)
    plt.plot(EMA60['Close Price'], label='EMA60', alpha=0.35)
    plt.title(stock + ' history (EMA)')
    plt.xlabel('01/01/2019 - ' + current_date)
    plt.ylabel('Close price')
    plt.legend(loc='upper left')
    plt.savefig('C:/Users/vital/PycharmProjects/tradeInfo/main/static/main/py/my_chart1.png')


def Upper_levels(stock_name):
    stock = stock_name
    country = 'ukraine'
    current_date = str(date.today().day) + '/'+ str(date.today().month) +'/' + str(date.today().year)
    try:
        df = investpy.get_stock_historical_data(stock = stock,country = country,from_date='01/01/2019',to_date=current_date)
    except:
        df = yf.download(stock,start ='2019-01-01',end = date.today(),progress=False)

    pivots = []
    dates = []
    counter = 0
    lastPivot = 0

    Range = [0,0,0,0,0,0,0,0,0,0]
    dateRange = [0,0,0,0,0,0,0,0,0,0]

    for i in df.index:
        currentMax = max(Range,default = 0)
        value = round(df['High'][i],2)

        Range = Range[1:9]
        Range.append(value)
        dateRange = dateRange[1:9]
        dateRange.append(i)

        if currentMax == max(Range,default = 0):
            counter+=1
        else:
            counter =0
        if counter == 5:
            lastPivot=currentMax
            dateloc = Range.index(lastPivot)
            lastDate = dateRange[dateloc]
            pivots.append(lastPivot)
            dates.append(lastDate)


    timeD = dt.timedelta(days=30)

    plt.figure(figsize = (12.6,4.6))
    plt.title(stock + ' history (upper levels)')
    plt.xlabel('01/01/2019 - '+ current_date)
    plt.ylabel('Close price')
    plt.plot(df['High'], label = stock ,alpha = 0.35)
    for index in range(len(pivots)):
        plt.plot_date([dates[index],dates[index]+timeD],[pivots[index],pivots[index]], linestyle ='-',linewidth = 2,marker = ",")
    plt.legend(loc = 'upper left')
    plt.savefig('C:/Users/vital/PycharmProjects/tradeInfo/main/static/main/py/my_chart2.png')


def Low_levels(stock_name):
    stock = stock_name
    country = 'ukraine'
    current_date = str(date.today().day) + '/'+ str(date.today().month) +'/' + str(date.today().year)
    try:
        df = investpy.get_stock_historical_data(stock = stock,country = country,from_date='01/01/2019',to_date=current_date)
    except:
        df = yf.download(stock,start ='2019-01-01',end = date.today(),progress=False)

    pivots = []
    dates = []
    counter = 0
    lastPivot = 0

    Range = [999999]*10
    dateRange = [0,0,0,0,0,0,0,0,0,0]

    for i in df.index:
        currentMin = min(Range,default = 0)
        value = round(df['Low'][i],2)

        Range = Range[1:9]
        Range.append(value)
        dateRange = dateRange[1:9]
        dateRange.append(i)

        if currentMin == min(Range,default = 0):
            counter+=1
        else:
            counter =0
        if counter == 5:
            lastPivot=currentMin
            dateloc = Range.index(lastPivot)
            lastDate = dateRange[dateloc]
            pivots.append(lastPivot)
            dates.append(lastDate)


    timeD = dt.timedelta(days=30)

    plt.figure(figsize = (12.6,4.6))
    plt.title(stock + ' history (low levels)')
    plt.xlabel('01/01/2019 - '+ current_date)
    plt.ylabel('Close price')
    plt.plot(df['Low'], label = stock ,alpha = 0.35)
    for index in range(len(pivots)):
        plt.plot_date([dates[index],dates[index]+timeD],[pivots[index],pivots[index]], linestyle ='-',linewidth = 2,marker = ",")
    plt.legend(loc = 'upper left')
    plt.savefig('C:/Users/vital/PycharmProjects/tradeInfo/main/static/main/py/my_chart3.png')


def Last_Month(stock_name):
    stock = stock_name
    country = 'ukraine'
    current_date = str(date.today().day) + '/'+ str(date.today().month) +'/' + str(date.today().year)
    try:
        df = investpy.get_stock_historical_data(stock = stock,country = country,from_date='01/01/2019',to_date=current_date)
    except:
        df = yf.download(stock,start ='2019-01-01',end = date.today(),progress=False)
    plt.figure(figsize = (12.6,4.6))
    plt.plot(df['Close'][-30:], label = stock ,alpha = 0.35)
    plt.title(stock + ' history last 30 days')
    plt.xlabel('Last 30 days')
    plt.ylabel('Close price')
    plt.legend(loc = 'upper left')
    plt.savefig('C:/Users/vital/PycharmProjects/tradeInfo/main/static/main/py/my_chart4.png')








