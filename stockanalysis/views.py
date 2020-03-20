# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
#import matplotlib.pyplot as plt
from matplotlib import pylab
from pylab import *
import pandas_datareader as web
import PIL, PIL.Image
from io import StringIO
import json
import unicodedata
import datetime
import requests
from bs4 import BeautifulSoup 
import csv
import pandas as pd
import sqlite3
from .models import stockdata,extrastock,mostloser
from .models import *
from .forms import *
from django.views.decorators.csrf import csrf_protect

### Calculate Dates Here####
d=str(datetime.date.today())
d1=d.split("-")
d2=[]
for i in range(len(d1)):
    d_en=d1[i].encode('ascii')
    d2.append(d_en)
#print(d2)
start=""
end=""
s1=""
e1=""
start1=""
for i in range(len(d2)):
    x=d2[i]+"-"
    e1=e1+x
end=e1[:len(s1)-1]
#print(end)
s_year=str(int(d2[0])-5)
start=s_year+"-"+d2[1]+"-"+d2[2]

user_name=""
user_salary=0
inv_type=""
user_ret=0
# Create your views here.
def home(request):

    return render(request,'index.html')


def index(request):

    d=str(datetime.date.today())
    d1=d.split("-")
    d2=[]
    for i in range(len(d1)):
        d_en=d1[i].encode('ascii')
        d2.append(d_en)
    #print(d2)
    start=""
    end=""
    s1=""
    e1=""
    for i in range(len(d2)):
        x=d2[i]+"-"
        e1=e1+x
    end=e1[:len(s1)-1]
    #print(end)
    s_year=str(int(d2[0])-1)
    start=s_year+"-"+d2[1]+"-"+d2[2]
    #print(start)
    stock=web.get_data_yahoo("^BSESN",start=start,end=end) #it fetches the stocks from in.finance.yahoo.com
    #print(stock.head())
    a=stock['Close']       
    a1=stock['Open']
    '''
    # Optional Snippet for getting data by months
    a1=a.resample('M').ffill()                   #Formats the regular data to monthly based data
    #print(a1)
    b=a1.reset_index()
    c=b['Date']
    d=c.to_string().split(" ")
    '''
    # Getting data by dates and fetch the dates
    b1=a.reset_index()
    
    c1=b1['Date']
    d1=c1.to_string().split(" ")
    date_list=[]
    for i in range(len(d1)):
        x=d1[i]
        if(len(x)>10):
            date_list.append(x)
    date=[]
    leng=[]
    for i in range(len(date_list)):
        x=date_list[i]
        y= x.encode("ascii")
        z=y.replace("-","/")
        z1=str(y)
        if (len(z)==12):
            date.append(z[:len(z)-2])              #List of dates
        elif (len(z)==13):
            date.append(z[:len(z)-3])
        else:
            date.append(z[:len(z)-4])
        leng.append(type(z))
    
    li=a.values.tolist()                         #converts the dataframe to list
    li_open=a1.values.tolist()
    ''' m1=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    cat_month=int(d2[1][0:])
    month=[]
    ye=str(int(d2[0][1:])-1)
    for i in range(len(m1)):
        x=m1[i]+"/"+ye
        month.append(x)
    for i in range(0,cat_month):
        x=m1[i]+"/"+d2[0][2:]
        month.append(str(x))
    '''
  
    stock_nse=web.get_data_yahoo("^NSEI",start=start,end=end) #it fetches the stocks from in.finance.yahoo.com
    #print(stock.head())
    nse_close=stock_nse['Close']       
    nse_open=stock_nse['Open']
    '''
    # Optional Snippet for getting data by months
    a1=a.resample('M').ffill()                   #Formats the regular data to monthly based data
    #print(a1)
    b=a1.reset_index()
    c=b['Date']
    d=c.to_string().split(" ")
    '''
    # Getting data by dates and fetch the dates
    b2=nse_close.reset_index()
    
    c2=b2['Date']
    d2=c2.to_string().split(" ")
    date_list2=[]
    for i in range(len(d2)):
        x=d2[i]
        if(len(x)>10):
            date_list2.append(x)
    date2=[]
    leng2=[]
    for i in range(len(date_list2)):
        x=date_list2[i]
        y= x.encode("ascii")
        z=y.replace("-","/")
        z1=str(y)
        if (len(z)==12):
            date2.append(z[:len(z)-2])              #List of dates
        elif (len(z)==13):
            date2.append(z[:len(z)-3])
        else:
            date2.append(z[:len(z)-4])
        leng2.append(type(z))
    
    nseli=nse_close.values.tolist()                         #converts the dataframe to list
    nseli_open=nse_open.values.tolist()
    
    
    
    # Code for scrapping in.finance.yahoo.com ---temparory

    #-----------------Completed---------------------------
   
    #----------------Additional Details-------------------'
    
    stock_nf=web.get_data_yahoo("^NSEI",start="2020-03-17",end="2020-03-17") #it fetches the stocks from in.finance.yahoo.com
    #print(stock.head())
    nf_price=[]
    dow_price=[]
    nas_price=[]
    bit_price=[]

    nf=stock_nf['Close']  
    n=nf.reset_index()     
    #print(n)
    nf_pr=nf.values.tolist()
    n1=round(nf_pr[0],4)
    nf_price.append(n1)
    #print(nf_price)
    stock_dow=web.get_data_yahoo("^DJI",start="2020-03-17",end="2020-03-17")
    dow=stock_dow['Close']
    d=dow.reset_index() 
    #print(d)
    dow_pr=dow.values.tolist()
    d1=round(dow_pr[0],4)
    dow_price.append(d1)

    stock_nas=web.get_data_yahoo("^IXIC",start="2020-03-17",end="2020-03-17")
    nas=stock_nas['Close']
    ns=nas.reset_index() 
    #print(ns)
    nas_pr=nas.values.tolist()
    ns1=round(nas_pr[0],4)
    nas_price.append(ns1)

    stock_bit=web.get_data_yahoo("BTC-INR",start="2020-03-17",end="2020-03-17")
    bit=stock_bit['Close']
    bt=bit.reset_index() 
    #print(bt)
    bit_pr=bit.values.tolist()
    bt1=round(bit_pr[0],2)
    bit_price.append(bt1)
   
    #----------------End of "Additional Details"----------
    #----------------Additional Details part-2------------
    stsymbol=[]
    stname=[]
    stprice=[]
    stchange=[]
    st_url="https://in.finance.yahoo.com/gainers"
    r1= requests.get(st_url)
    data1=r1.text
    soup1=BeautifulSoup(data1)
    for listing in soup1.find_all('tr',attrs={'class':'simpTblRow Bgc($extraLightBlue):h BdB Bdbc($finLightGrayAlt) Bdbc($tableBorderBlue):h H(32px) Bgc(white)'}):
        for symbol in listing.find_all('td',attrs={'aria-label':'Symbol'}):
            stsymbol.append(symbol.text)
        for names in listing.find_all('td',attrs={'aria-label':'Name'}):
            stname.append(names.text)
        for prices in listing.find_all('td',attrs={'aria-label':'Price (intraday)'}):
            stprice.append(prices.text)
        for changes in listing.find_all('td',attrs={'aria-label':'Change'}):
            stchange.append(changes.text)
    st_symbol=[]  
    st_name=[]
    st_price=[]
    st_change=[]

    for i in range(len(stname)):
        x=stsymbol[i].encode('ascii')
        y=stname[i].encode('ascii')
        z=stprice[i].encode('ascii')
        p=stchange[i].encode('ascii')
        st_symbol.append(x)
        st_name.append(y)
        st_price.append(z)
        st_change.append(p)
    for i in range(len(st_name)):
        symbol1=st_symbol[i]
        name1=st_name[i]
        price1=st_price[i]
        change1=st_change[i]
        data_instance=extrastock.objects.create(symbol=symbol1,name=name1,price=price1,change=change1)
    extra_data=extrastock.objects.all()


    lname=[]
    lprice=[]
    lchange=[]
    l_url="https://in.finance.yahoo.com/losers"
    r2= requests.get(l_url)
    data2=r2.text
    soup2=BeautifulSoup(data2)
    for listing in soup2.find_all('tr',attrs={'class':'simpTblRow Bgc($extraLightBlue):h BdB Bdbc($finLightGrayAlt) Bdbc($tableBorderBlue):h H(32px) Bgc(white)'}):
        for names in listing.find_all('td',attrs={'aria-label':'Name'}):
            lname.append(names.text)
        for prices in listing.find_all('td',attrs={'aria-label':'Price (intraday)'}):
            lprice.append(prices.text)
        for changes in listing.find_all('td',attrs={'aria-label':'Change'}):
            lchange.append(changes.text)
      
    l_name=[]
    l_price=[]
    l_change=[]
    trashname=[]
    trashprice=[]
    trashchange=[]
    for i in range(len(lname)):
        try:
            y=lname[i].encode('ascii')
            z=lprice[i].encode('ascii')
            p=lchange[i].encode('ascii')
            l_name.append(y)
            l_price.append(z)
            l_change.append(p)
        except:
            trashname.append(lname[i])
            trashprice.append(lprice[i])
            trashchange.append(lchange[i])
    for i in range(len(l_name)):
        name1=l_name[i]
        price1=l_price[i]
        change1=l_change[i]
        data_instance=mostloser.objects.create(name=name1,price=price1,change=change1)
    stock_loser=mostloser.objects.all()
    #----------------End of "Additional Details part-2"---

    


    return render(request,'index.html',{        #pass the json based data to response
        'data':li,
        'date' : date,
        'data_open': li_open,
        'nifty': nf_price,
        'dow': dow_price,
        'nasdaq': nas_price,
        'bitcoin': bit_price,
        'nsedata': nseli,
        'datense':date2,
        'nseopen':nse_open,
        'extradata':extra_data[:25],
        'stockloser':stock_loser[:25],
    })

def delete():
    stockdata.objects.all().delete()
    extrastock.objects.all().delete()
    yearlyrecom.objects.all().delete()
    monthlyrecom.objects.all().delete()
    return "Entry deleted!!!"

def form1(request):
    if request.method=="POST":
        username=request.POST['username'].encode('ascii')
        password=request.POST['password'].encode('ascii')
        name=request.POST['name'].encode('ascii')
        email=request.POST['email'].encode('ascii')	
        phone=request.POST['phone'].encode('ascii')
        job=request.POST['job'].encode('ascii')
        income=request.POST['income'].encode('ascii')
        span=request.POST['span'].encode('ascii')
        problem=request.POST['problem'].encode('ascii')
        ex_return=request.POST['ex_return'].encode('ascii')

        user1=userinfo.objects.create(username=username,password=password,name=name,email=email,phone=phone,job=job,income=income,span=span,problem=problem,ex_return=ex_return)
        user1.save()
        return redirect('/login/')
    else:
        print('Error from getting Requests!!!!')
    return render(request,'sign-up.html')

def login(request):
    del_data=delete()
    print(del_data)
    if request.method=='POST':
        username=request.POST['username'].encode('ascii')
        password=request.POST['password'].encode('ascii')
        if userinfo.objects.filter(username=username,password=password).exists():
            user=userinfo.objects.get(username=username)
            global user_name,user_salary,inv_type,user_ret
            user_name=username
            print(user_name)
            #user_income=user.income
            user_salary=user.income
            print(user_salary)
            inv_type=user.span
            print(inv_type)
            user_ret=float(user.ex_return)
            print(user_ret)
            return redirect('/home/',{'user': user_name})
        else:
            context={'msg':'Invalid username or password'}
            return render(request,'login.html',context)
    return render(request,'login.html')


def recommand(request):

    global user_name,user_salary,inv_type,user_ret
    print(user_name)
    print(user_salary)
    print(inv_type)
    print(user_ret)
    symbol=[]
    name=[] 
    price=[]
    change=[]
    volume=[]
    '''
    del_data=delete()
    print(del_data)
    '''
    stock_url="https://in.finance.yahoo.com/most-active"
    r= requests.get(stock_url)
    data=r.text
    soup=BeautifulSoup(data)
    for listing in soup.find_all('tr',attrs={'class':'simpTblRow Bgc($extraLightBlue):h BdB Bdbc($finLightGrayAlt) Bdbc($tableBorderBlue):h H(32px) Bgc(white)'}):
        for symbols in listing.find_all('td',attrs={'aria-label':'Symbol'}):
            symbol.append(symbols.text)
        for names in listing.find_all('td',attrs={'aria-label':'Name'}):
            name.append(names.text)
        for prices in listing.find_all('td',attrs={'aria-label':'Price (intraday)'}):
            price.append(prices.text)
        for changes in listing.find_all('td',attrs={'aria-label':'Change'}):
            change.append(changes.text)
        for vol in listing.find_all('td',attrs={'aria-label':'Volume'}):
            volume.append(vol.text)
    s_symbol=[]
    s_name=[]
    s_price=[]
    s_change=[]
    s_volume=[]

    for i in range(len(symbol)):
        x=symbol[i].encode('ascii')
        y=name[i].encode('ascii')
        z=price[i].encode('ascii')
        p=change[i].encode('ascii')
        q=volume[i].encode('ascii')
        s_symbol.append(x)
        s_name.append(y)
        s_price.append(z)
        s_change.append(p)
        s_volume.append(q)
    for i in range(len(s_symbol)):
        symbol1=s_symbol[i]
        name1=s_name[i]
        price1=s_price[i]
        change1=s_change[i]
        vol1=s_volume[i]
        data_instance=stockdata.objects.create(symbol=symbol1,name=name1,price=price1,change=change1,volume=vol1)
        datas=stockdata.objects.all()
    print("Im in recommandation section ")
    salary=user_salary
    i_type=inv_type
    print(i_type)
    ex_return=user_ret
    print(ex_return)
    ################ Calculating Recommendations on the basis of span type ############
    ################### Monthly and Weekly Started ####################################
    if(i_type=="weekly" or i_type=="Weekly" or i_type=="monthly" or i_type=="Monthly"):
        sal=salary
        typ=i_type
        eret=ex_return
        stock_list=[]

        index_temp=[]
        saving=((5 * salary)/100)
        no_stocks=0
        for data in extrastock.objects.raw('SELECT * FROM stockanalysis_extrastock'):
            a=data.symbol
            index_temp.append(a.encode('ascii'))
        temp=set(index_temp)
        index=list(temp)
        cl_price=[]
        print(index)
        for i in range(len(index)):
            trash=[]
            try:
                stock=web.get_data_yahoo(index[i],start="2020-03-05",end="2020-03-05")
                price=stock['Adj Close'].tolist()
                x=price[0]
                if(x>=100):
                    stock_list.append(index[i])
                    n=saving/x
                    no_stocks=n
                    cl_price.append(int(n))
            except Exception as e:
                trash.append(index[i])
                print("Deleted!!")
                print
                print(e)

        print("Limit of stock:",no_stocks)
        print(stock_list)
        #print(cl_price)

        s_month=str(int(d2[1])-1)
        start1=d2[0]+"-"+s_month+"-"+d2[2]
        # for calculating weekly returns
        default_limit=10
        shortlist1=[]
        shortlist2=[]
        ret2=[]
        for i in range(len(stock_list)):
            symbol=stock_list[i]
            if(typ=="weekly" or typ=="Weekly"):
                re1=[]
                re2=[]
                trash=[]
                try:
                    stock_url = web.get_data_yahoo(symbol,start = start1,end = "2020-03-16")
                    weekly_returns=stock_url['Adj Close'].resample('W').ffill().pct_change().values.tolist()[1:]
                    try:
                        x=0
                        for i in range(len(weekly_returns)):
                            x=x+weekly_returns[i]
                        avg_ret=x/len(weekly_returns)
                    except:
                        trash.append(avg_ret)
                    ret=avg_ret * default_limit

                    if(ret>0):
                        shortlist1.append(symbol)
                        ret1.append(ret)
                    if(ret>-1 and ret<0):
                        shortlist2.append(symbol)
                        ret2.append(ret)
                    else:
                        pass
                except:
                    trash.append(symbol)
            else:
                trash=[]
                re1=[]
                re2=[]
                try:
                    stock_url2 = web.get_data_yahoo(symbol,start = "2019-10-03",end = "2020-03-16")
                    monthly_returns=stock_url2['Adj Close'].resample('M').ffill().pct_change().values.tolist()[1:]
                    try:
                        x=0
                        for i in range(len(monthly_returns)):
                            x=x+monthly_returns[i]
                        avg_ret=x/len(monthly_returns)
                    except:
                        trash.append(avg_ret)
                    ret=avg_ret * default_limit

                    if(ret>0):
                        shortlist1.append(symbol)
                        ret1.append(ret)
                    if(ret>-1 and ret<0):
                        shortlist2.append(symbol)
                        ret2.append(ret)
                    else:
                        pass
                except:
                    trash.append(symbol)
        final_stock1=[]
        final_ret1=[]
        print
        print(shortlist2)
        for i in range(len(shortlist2)):
            symbol=shortlist2[i]
            s_ret=ret2[i]*(-1)
            #stock=web.get_data_yahoo(symbol,start=end,end=end)
            #price=stock['Adj Close'].tolist()
            x=1-s_ret
            print x
            if(x<=1):
                final_stock1.append(symbol)
                final_ret1.append(ret2[i])
            else:
                pass
        print(final_stock1)
        print "For ",typ," period, recommanded stocks are as under:"

        for i in range(len(final_stock1)):
            temp1=[]
            name=[]
            symbol=final_stock1[i]
            for data in extrastock.objects.raw('SELECT * FROM  stockanalysis_extrastock WHERE symbol= %s',[symbol]):
                x=data.name
                temp1.append(x.encode('ascii'))
            a=set(temp1)
            name=list(a)
            store_data=monthlyrecom.objects.create(symbol=symbol,stockname=name[0],rrate=final_ret1[i])
            datas1=monthlyrecom.objects.all()
          
        return render(request,'recommand1.html',{        #pass the json based data to response
            'stock': datas1,
            'name': temp1,
        })


    ######################### Monthly and Weekly Completed #################
    ######################## Yearly Start ##################################
    elif(i_type=="yearly" or i_type=="Yearly"):
        sal=salary
        typ=i_type
        eret=ex_return
        stock_list=[]
        cl_price=[]
        '''
        con= sqlite3.connect('/home/ubuntu/project/test_3/db.sqlite3')
        cursor=con.cursor()
        cursor.execute('SELECT * FROM stockanalysis_extrastock')
        '''
        #data_raw=extrastock.objects.all()
        
        #print(rows)
        index_temp=[]
        final_stock=[]
        final_ret=[]
        final_shares=[]
        saving=((5 * salary)/100)
        no_stocks=0
        limit=0
        for data in stockdata.objects.raw('SELECT * FROM stockanalysis_stockdata'):
            a=data.symbol
            index_temp.append(a.encode('ascii'))
        '''
        for row in rows:
            #print(row)
            r=list(row)
            #print(r)
            x=r[4].encode('ascii')
            index_temp.append(x)
        '''
        temp=set(index_temp)
        index=list(temp)
        print(index)
        for i in range(len(index)):
            trash=[]
            try:
                stock=web.get_data_yahoo(index[i],start="2020-03-17",end="2020-03-17")
                price=stock['Adj Close'].tolist()
                x=price[0]
                if(x>=100):
                    stock_list.append(index[i])
                    n=saving/x
                    no_stocks=n
                    limit=int(n)
                    cl_price.append(int(n))
            except:
                trash.append(index[i])
                print("Deleted!!")
        print("Limit of stock:",no_stocks)
        print(stock_list)
        print(cl_price)
        shortlist2=[]
        shortlist1=[]
        ret1=[]
        ret2=[]
        ret_def=[]
        for i in range(len(stock_list)):
            symbol=stock_list[i]
            stock_url1 = web.get_data_yahoo(symbol,start = start,end = "2020-03-17")
            yearly_returns=stock_url1['Adj Close'].resample('Y').ffill().pct_change()
            #print(yearly_returns)
            y=yearly_returns.values.tolist()
            yer=y[1:]
            default_limit=10
            trash=[]

            if(typ=="yearly" or typ=="Yearly"):
                try:
                    x=0
                    for i in range(len(yer)):
                        x=x+yer[i]
                    avg_ret=x/len(yer)

                except:
                    trash.append(avg_ret)
                    #print(symbol)
            ret=avg_ret * default_limit

            if(ret>0):
                shortlist1.append(symbol)
                ret1.append(ret)
            if(ret>-1 and ret<0):
                shortlist2.append(symbol)
                ret2.append(ret)
            else:
                pass
        print(len(shortlist1))
        print
        print(len(ret1))
        for i in range(len(shortlist1)):
            trash=[]
            symbol=shortlist1[i]
            try:   
                s_ret=ret1[i]
                stock=web.get_data_yahoo(symbol,start="2020-03-17",end="2020-03-17")
                price=stock['Adj Close'].tolist()
                x=price[0]
                print(x)
                a1=(saving*7.33)/10
                no_stocks=int(a1/x)
                print(no_stocks)

                tot_ret=(no_stocks*s_ret)/10
                e=int((eret*no_stocks)/tot_ret)
                print "No of stocks:",e
                e1=e*s_ret
                print "Return:",e1
                if(e1>=eret and e<=limit):
                    final_stock.append(symbol)
                    final_ret.append(float(s_ret/10))
                    final_shares.append(e)
                else:
                    pass
            except Exception as e:
                trash.append(symbol)
                print e
                print('a:',symbol)
        print "To satisfy your expectation, we will provide the amount of shares you have to buy:"
        for i in range(len(final_stock)):
            temp1=[]
            name=[]
            symbol=final_stock[i]
            for data in stockdata.objects.raw('SELECT * FROM  stockanalysis_stockdata WHERE symbol= %s',[symbol]):
                x=data.name
                temp1.append(x.encode('ascii'))
            a=set(temp1)
            name=list(a)
            store_data=yearlyrecom.objects.create(symbol=symbol,name=name[0],quantity=final_shares[i],rrate=final_ret[i])
            datas2=yearlyrecom.objects.all()

        return render(request,'recommand.html',{        #pass the json based data to response
            'stock': datas2,
        })
    return render(request,'recommand.html',{        #pass the json based data to response
        'stock': datas,
    })


def index2(request):
   
    d=str(datetime.date.today())
    d1=d.split("-")
    d2=[]
    for i in range(len(d1)):
        d_en=d1[i].encode('ascii')
        d2.append(d_en)
    #print(d2)
    start=""
    end=""
    s1=""
    e1=""
    for i in range(len(d2)):
        x=d2[i]+"-"
        e1=e1+x
    end=e1[:len(s1)-1]
    #print(end)
    s_year=str(int(d2[0])-1)
    start=s_year+"-"+d2[1]+"-"+d2[2]
    #print(start)
    stock=web.get_data_yahoo("^BSESN",start=start,end=end) #it fetches the stocks from in.finance.yahoo.com
    #print(stock.head())
    a=stock['Close']       
    a1=stock['Open']
    '''
    # Optional Snippet for getting data by months
    a1=a.resample('M').ffill()                   #Formats the regular data to monthly based data
    #print(a1)
    b=a1.reset_index()
    c=b['Date']
    d=c.to_string().split(" ")
    '''
    # Getting data by dates and fetch the dates
    b1=a.reset_index()
    
    c1=b1['Date']
    d1=c1.to_string().split(" ")
    date_list=[]
    for i in range(len(d1)):
        x=d1[i]
        if(len(x)>10):
            date_list.append(x)
    date=[]
    leng=[]
    for i in range(len(date_list)):
        x=date_list[i]
        y= x.encode("ascii")
        z=y.replace("-","/")
        z1=str(y)
        if (len(z)==12):
            date.append(z[:len(z)-2])              #List of dates
        elif (len(z)==13):
            date.append(z[:len(z)-3])
        else:
            date.append(z[:len(z)-4])
        leng.append(type(z))
    
    li=a.values.tolist()                         #converts the dataframe to list
    li_open=a1.values.tolist()
    ''' m1=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    cat_month=int(d2[1][0:])
    month=[]
    ye=str(int(d2[0][1:])-1)
    for i in range(len(m1)):
        x=m1[i]+"/"+ye
        month.append(x)
    for i in range(0,cat_month):
        x=m1[i]+"/"+d2[0][2:]
        month.append(str(x))
    '''
  
    stock_nse=web.get_data_yahoo("^NSEI",start=start,end=end) #it fetches the stocks from in.finance.yahoo.com
    #print(stock.head())
    nse_close=stock_nse['Close']       
    nse_open=stock_nse['Open']
    '''
    # Optional Snippet for getting data by months
    a1=a.resample('M').ffill()                   #Formats the regular data to monthly based data
    #print(a1)
    b=a1.reset_index()
    c=b['Date']
    d=c.to_string().split(" ")
    '''
    # Getting data by dates and fetch the dates
    b2=nse_close.reset_index()
    
    c2=b2['Date']
    d2=c2.to_string().split(" ")
    date_list2=[]
    for i in range(len(d2)):
        x=d2[i]
        if(len(x)>10):
            date_list2.append(x)
    date2=[]
    leng2=[]
    for i in range(len(date_list2)):
        x=date_list2[i]
        y= x.encode("ascii")
        z=y.replace("-","/")
        z1=str(y)
        if (len(z)==12):
            date2.append(z[:len(z)-2])              #List of dates
        elif (len(z)==13):
            date2.append(z[:len(z)-3])
        else:
            date2.append(z[:len(z)-4])
        leng2.append(type(z))
    
    nseli=nse_close.values.tolist()                         #converts the dataframe to list
    nseli_open=nse_open.values.tolist()
    
    
    
    # Code for scrapping in.finance.yahoo.com ---temparory
    '''
    if(stockdata.objects.all().count()>0):
        dele=delete()
        print(dele)
    
    symbol=[]
    name=[] 
    price=[]
    change=[]
    volume=[]


    stock_url="https://in.finance.yahoo.com/most-active"
    r= requests.get(stock_url)
    data=r.text
    soup=BeautifulSoup(data)
    for listing in soup.find_all('tr',attrs={'class':'simpTblRow Bgc($extraLightBlue):h BdB Bdbc($finLightGrayAlt) Bdbc($tableBorderBlue):h H(32px) Bgc(white)'}):
        for symbols in listing.find_all('td',attrs={'aria-label':'Symbol'}):
            symbol.append(symbols.text)
        for names in listing.find_all('td',attrs={'aria-label':'Name'}):
            name.append(names.text)
        for prices in listing.find_all('td',attrs={'aria-label':'Price (intraday)'}):
            price.append(prices.text)
        for changes in listing.find_all('td',attrs={'aria-label':'Change'}):
            change.append(changes.text)
        for vol in listing.find_all('td',attrs={'aria-label':'Volume'}):
            volume.append(vol.text)
    s_symbol=[]
    s_name=[]
    s_price=[]
    s_change=[]
    s_volume=[]

    for i in range(len(symbol)):
        x=symbol[i].encode('ascii')
        y=name[i].encode('ascii')
        z=price[i].encode('ascii')
        p=change[i].encode('ascii')
        q=volume[i].encode('ascii')
        s_symbol.append(x)
        s_name.append(y)
        s_price.append(z)
        s_change.append(p)
        s_volume.append(q)
    for i in range(len(s_symbol)):
        symbol1=s_symbol[i]
        name1=s_name[i]
        price1=s_price[i]
        change1=s_change[i]
        vol1=s_volume[i]
        data_instance=stockdata.objects.create(symbol=symbol1,name=name1,price=price1,change=change1,volume=vol1)
   
    '''
    #-----------------Completed---------------------------
   
    #----------------Additional Details-------------------'
    
    stock_nf=web.get_data_yahoo("^NSEI",start="2020-03-17",end="2020-03-17") #it fetches the stocks from in.finance.yahoo.com
    #print(stock.head())
    nf_price=[]
    dow_price=[]
    nas_price=[]
    bit_price=[]

    nf=stock_nf['Close']  
    n=nf.reset_index()     
    #print(n)
    nf_pr=nf.values.tolist()
    n1=round(nf_pr[0],4)
    nf_price.append(n1)
    #print(nf_price)
    stock_dow=web.get_data_yahoo("^DJI",start="2020-03-17",end="2020-03-17")
    dow=stock_dow['Close']
    d=dow.reset_index() 
    #print(d)
    dow_pr=dow.values.tolist()
    d1=round(dow_pr[0],4)
    dow_price.append(d1)

    stock_nas=web.get_data_yahoo("^IXIC",start="2020-03-17",end="2020-03-17")
    nas=stock_nas['Close']
    ns=nas.reset_index() 
    #print(ns)
    nas_pr=nas.values.tolist()
    ns1=round(nas_pr[0],4)
    nas_price.append(ns1)

    stock_bit=web.get_data_yahoo("BTC-INR",start="2020-03-17",end="2020-03-17")
    bit=stock_bit['Close']
    bt=bit.reset_index() 
    #print(bt)
    bit_pr=bit.values.tolist()
    bt1=round(bit_pr[0],2)
    bit_price.append(bt1)
   
    #----------------End of "Additional Details"----------
    #----------------Additional Details part-2------------
    stsymbol=[]
    stname=[]
    stprice=[]
    stchange=[]
    st_url="https://in.finance.yahoo.com/gainers"
    r1= requests.get(st_url)
    data1=r1.text
    soup1=BeautifulSoup(data1)
    for listing in soup1.find_all('tr',attrs={'class':'simpTblRow Bgc($extraLightBlue):h BdB Bdbc($finLightGrayAlt) Bdbc($tableBorderBlue):h H(32px) Bgc(white)'}):
        for symbol in listing.find_all('td',attrs={'aria-label':'Symbol'}):
            stsymbol.append(symbol.text)
        for names in listing.find_all('td',attrs={'aria-label':'Name'}):
            stname.append(names.text)
        for prices in listing.find_all('td',attrs={'aria-label':'Price (intraday)'}):
            stprice.append(prices.text)
        for changes in listing.find_all('td',attrs={'aria-label':'Change'}):
            stchange.append(changes.text)
    st_symbol=[]  
    st_name=[]
    st_price=[]
    st_change=[]

    for i in range(len(stname)):
        x=stsymbol[i].encode('ascii')
        y=stname[i].encode('ascii')
        z=stprice[i].encode('ascii')
        p=stchange[i].encode('ascii')
        st_symbol.append(x)
        st_name.append(y)
        st_price.append(z)
        st_change.append(p)
    for i in range(len(st_name)):
        symbol1=st_symbol[i]
        name1=st_name[i]
        price1=st_price[i]
        change1=st_change[i]
        data_instance=extrastock.objects.create(symbol=symbol1,name=name1,price=price1,change=change1)
    extra_data=extrastock.objects.all()


    lname=[]
    lprice=[]
    lchange=[]
    l_url="https://in.finance.yahoo.com/losers"
    r2= requests.get(l_url)
    data2=r2.text
    soup2=BeautifulSoup(data2)
    for listing in soup2.find_all('tr',attrs={'class':'simpTblRow Bgc($extraLightBlue):h BdB Bdbc($finLightGrayAlt) Bdbc($tableBorderBlue):h H(32px) Bgc(white)'}):
        for names in listing.find_all('td',attrs={'aria-label':'Name'}):
            lname.append(names.text)
        for prices in listing.find_all('td',attrs={'aria-label':'Price (intraday)'}):
            lprice.append(prices.text)
        for changes in listing.find_all('td',attrs={'aria-label':'Change'}):
            lchange.append(changes.text)
      
    l_name=[]
    l_price=[]
    l_change=[]
    trashname=[]
    trashprice=[]
    trashchange=[]
    for i in range(len(lname)):
        try:
            y=lname[i].encode('ascii')
            z=lprice[i].encode('ascii')
            p=lchange[i].encode('ascii')
            l_name.append(y)
            l_price.append(z)
            l_change.append(p)
        except:
            trashname.append(lname[i])
            trashprice.append(lprice[i])
            trashchange.append(lchange[i])
    for i in range(len(l_name)):
        name1=l_name[i]
        price1=l_price[i]
        change1=l_change[i]
        data_instance=mostloser.objects.create(name=name1,price=price1,change=change1)
    stock_loser=mostloser.objects.all()
    #----------------End of "Additional Details part-2"---

    


    return render(request,'home.html',{        #pass the json based data to response
        'data':li,
        'date' : date,
        'data_open': li_open,
        'nifty': nf_price,
        'dow': dow_price,
        'nasdaq': nas_price,
        'bitcoin': bit_price,
        'nsedata': nseli,
        'datense':date2,
        'nseopen':nse_open,
        'extradata':extra_data[:25],
        'stockloser':stock_loser[:25],
    })