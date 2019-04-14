# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User, Order
import json
import requests
'''
accesscode = request.GET.get('code')
redirect_uri = 'http://www.example.com'
# ... your code ...


r = requests.post(url)
print(r.status_code)
print(r.text)
'''

def makeOrder(request):
	pass



def hello(request):


	if(request.method=='POST'):	
		print("IN POST")


	'''
	#accesscode = request.POST.get('code')
	accesscodetransfer = '1a78b180f18bf8b26d3f8a2c5254e557da7a34267521f6c457a31b6e1cb200f5'
	accesscodeaccounts = 'f3991bc69d2e99aff000cddad3de5f07f9801699ac19c8f20fe1df1a9fba4002'	
	redirect_uri = 'https://www.ahmetsutbas.com.tr/callback'
	url = 'https://idprep.kuveytturk.com.tr/api/connect/authorize?client_id=7cd8964b46564b12a6bbec30d96bfcfc&scope=accounts%20offline_access&response_type=code&redirect_uri=https://www.ahmetsutbas.com.tr/callback&state=abc'
	tokenurl = 'https://idprep.kuveytturk.com.tr/api/connect/token'

	# ... your code ...
	
	postdata = {
	    'grant_type': 'authorization_code',
	    'code': accesscodetransfer,
	    'redirect_uri': redirect_uri,
	    'client_id': '7cd8964b46564b12a6bbec30d96bfcfc',
	    'client_secret': 'SUZlZi888iJlt8ppuvsCghDIW59Xtdh8b67agPaZAbKBKLEYd4SpCA==',
	}

	headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': ('Bearer ' + accesscodetransfer)}

	r = requests.post(url,data=json.dumps(postdata),headers=headers)
	print(r.status_code)
	print(r.text)
	print(r)
	'''

	client_id = '7cd8964b46564b12a6bbec30d96bfcfc'
	client_secret = 'SUZlZi888iJlt8ppuvsCghDIW59Xtdh8b67agPaZAbKBKLEYd4SpCA'
	redirect_uri = 'https://www.ahmetsutbas.com.tr/callback'


	userSuffix = 2
	accessTokenAccounts = '3198ea741c417cfa9c851694f210c5dc4900d6215d3dd14c6470cbaffe82de13'
	urlToken = 'https://apitest.kuveytturk.com.tr/prep/v1/transfers/toIBAN'
	urlAccounts = 'https://apitest.kuveytturk.com.tr/prep/v1/accounts/' + str(userSuffix)
	
	data = {}
	
	headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + accessTokenAccounts)}

	r = requests.get(urlAccounts,data=json.dumps(data),headers=headers)
	#print(r.json())
	print()
	#balance = r.content[value]
	#print(balance)

	body = {
	   "SenderAccountSuffix":1,
	   "ReceiverName":"Dohn",
	   "ReceiverIBAN":"TR180001000909536286939001",
	   "Amount":3,
	   "Comment":"test money transfer",
		"PaymentTypeId":99  
	}





	print(request.POST)
	if request.POST and request.POST['amount'] != 0.0:
		print(request.POST)
		p = Order.objects.create(user_id=1, amount=1120, price=5.7909)
		p.save()


	if 0:
		p = User.objects.create(user_id=1, name='Ahmet', iban='TR50000')
		p.save()


	user_id = ""
	amount=""
	price=""
	buyOrSell=""
	submitted =""
	time=""
	p = Order.objects.filter(user_id=1)
	if p:
		p = p.first()
		user_id = p.user_id
		amount = p.amount
		price = p.price
		buyOrSell = "Satış"
		time="14.04.2019-13:30"
	context = {
		'order_id' : 1,
		'user_id' : user_id,
		'amount': amount,
		'price ': price,
		'submitted': submitted,
		'buyOrSell': buyOrSell,
		'time': time	}


	return render(request, "1.html", context)

def test(request):
	return render(request, "2.html")
	#username = request.POST[https://idprep.kuveytturk.com.tr/api/connect/token?grant_type=authorization_code&code=5161656&redirect_uri=local&client_id=4515&client_secret=1415151]
		#print(username)>

	#if(request.method=='POST'):
	#	redirect(hello)
	#url ='https://idprep.kuveytturk.com.tr/api/connect/authorize?client_id=7cd8964b46564b12a6bbec30d96bfcfc&scope=accounts%20offline_access&response_type=code&redirect_uri=https://www.ahmetsutbas.com.tr/callback&state=abc'
	#return redirect(url)	

def test2(request):
	print("aADSFASDFADFADFAFADFDF")



def demouser_2(request):


	if(request.method=='POST'):	
		print("IN POST")


	'''
	#accesscode = request.POST.get('code')
	accesscodetransfer = '1a78b180f18bf8b26d3f8a2c5254e557da7a34267521f6c457a31b6e1cb200f5'
	accesscodeaccounts = 'f3991bc69d2e99aff000cddad3de5f07f9801699ac19c8f20fe1df1a9fba4002'	
	redirect_uri = 'https://www.ahmetsutbas.com.tr/callback'
	url = 'https://idprep.kuveytturk.com.tr/api/connect/authorize?client_id=7cd8964b46564b12a6bbec30d96bfcfc&scope=accounts%20offline_access&response_type=code&redirect_uri=https://www.ahmetsutbas.com.tr/callback&state=abc'
	tokenurl = 'https://idprep.kuveytturk.com.tr/api/connect/token'

	# ... your code ...
	
	postdata = {
	    'grant_type': 'authorization_code',
	    'code': accesscodetransfer,
	    'redirect_uri': redirect_uri,
	    'client_id': '7cd8964b46564b12a6bbec30d96bfcfc',
	    'client_secret': 'SUZlZi888iJlt8ppuvsCghDIW59Xtdh8b67agPaZAbKBKLEYd4SpCA==',
	}

	headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': ('Bearer ' + accesscodetransfer)}

	r = requests.post(url,data=json.dumps(postdata),headers=headers)
	print(r.status_code)
	print(r.text)
	print(r)
	'''

	client_id = '7cd8964b46564b12a6bbec30d96bfcfc'
	client_secret = 'SUZlZi888iJlt8ppuvsCghDIW59Xtdh8b67agPaZAbKBKLEYd4SpCA'
	redirect_uri = 'https://www.ahmetsutbas.com.tr/callback'


	userSuffix = 2
	accessTokenAccounts = '3198ea741c417cfa9c851694f210c5dc4900d6215d3dd14c6470cbaffe82de13'
	urlToken = 'https://apitest.kuveytturk.com.tr/prep/v1/transfers/toIBAN'
	urlAccounts = 'https://apitest.kuveytturk.com.tr/prep/v1/accounts/' + str(userSuffix)
	
	data = {}
	
	headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + accessTokenAccounts)}

	r = requests.get(urlAccounts,data=json.dumps(data),headers=headers)
	#print(r.json())
	print()
	#balance = r.content[value]
	#print(balance)

	body = {
	   "SenderAccountSuffix":1,
	   "ReceiverName":"Dohn",
	   "ReceiverIBAN":"TR180001000909536286939001",
	   "Amount":3,
	   "Comment":"test money transfer",
		"PaymentTypeId":99  
	}


	if request.POST and request.POST['amount'] != 0.0:
		print(request.POST)
		p = Order.objects.create(user_id=2, amount=request.POST['amount'], price=5.7909)
		p.save()


	if 0:
		p = User.objects.create(user_id=2, name='Ahmet', iban='TR50000')
		p.save()


	user_id = ""
	amount=""
	price=""
	buyOrSell=""
	submitted =""
	time=""
	p = Order.objects.filter(user_id=2)
	if p:
		p = p.first()
		user_id = p.user_id
		amount = p.amount
		price = p.price
		buyOrSell = "Alış"
		time="14.04.2019-13:30"
	context = {
		'order_id' : 3,
		'user_id' : user_id,
		'amount': amount,
		'price ': price,
		'submitted': submitted,
		'buyOrSell': buyOrSell,
		'time': time	}


	return render(request, "3.html")