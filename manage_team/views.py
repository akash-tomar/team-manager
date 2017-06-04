# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login as log
from django.contrib.auth import logout as loggedout
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import authenticate
from django.http import JsonResponse
from .models import *
import re
from django.db.models import Q
import uuid
# Create your views here.

'''This function adds the member to the team'''

def verifyEmail(email):
	return True

@csrf_exempt
def addMember(request):
	if request.method=='POST':
		data = request.body
		data = json.loads(data)

		first_name = data["first_name"]
		last_name = data["last_name"]
		email = data["email"]
		role = data["role"]
		phone = data["phone"]
		
		role_num=1
		if role.lower()=="admin":
			role_num=0

		if not verifyEmail(email):
			return JsonResponse({"failed":"invalid attribute values"})

		# if user is not None:
		try:
			member = Member(first_name=first_name,last_name=last_name,email=email,phone=phone,role=role_num)
			member.save()
		except:
			return JsonResponse({"failed":"invalid attribute values"})

		return JsonResponse({"id":member.id,"first_name":member.first_name,"last_name":member.last_name,"email":member.email,"phone":member.phone,"role":role})


'''This function deletes the team member'''
@csrf_exempt
def deleteMember(request):
	if request.method=="DELETE":
		data = request.body
		data = json.loads(data)
		id_member = data["id"]
		try:
			member = Member.objects.get(pk=id_member)
			member.delete()
			return JsonResponse({})
		except:
			return JsonResponse({"failed":"Invalid id"})

'''This function can be used to update the product details'''
@csrf_exempt
def update(request):
	if request.method=='POST':
		data = request.body
		data = json.loads(data)

		id_member = data["id"]

		member=None
		try:
			member = Member.objects.get(pk=id_member)
		except:
			return JsonResponse({"failed":"invalid id"})

		first_name = data["first_name"]
		last_name = data["last_name"]
		email = data["email"]
		role = data["role"]
		phone = data["phone"]

		# if first_name is not None:


		prod = None
		try:
			prod = Product.objects.get(product_name=product_name,seller_name=seller_name)
		except:
			return JsonResponse({"success":False,"reason":"Invalid couple of product and seller name."})

		if "price" in data:
			prod.price=data["price"]
		if "quantity" in data:
			prod.quantity=data['quantity']
		if 'category' in data:
			prod.category.clear()
			for i in data["category"]:
				Tag.objects.get_or_create(name=i)
				prod.category.add(Tag.objects.get(name=i))
		prod.save()
		return JsonResponse({"success":True})

'''This function can be used to view the product details'''
@csrf_exempt
def getProduct(request):
	if not checkToken(request):
		return JsonResponse({"success":False,"reason":"authentication failed"})

	if request.method=="GET":
		product_name = request.GET.get("product_name")
		seller_name = request.GET.get("seller_name")
		try:
			prod = Product.objects.get(product_name=product_name,seller_name=seller_name)
			category_list=[]
			for i in prod.category.all():
				category_list.append(i.name)
			return JsonResponse({"success":True,"product":{"product_name":prod.product_name,
				"seller_name":prod.seller_name,"quantity":prod.quantity,"price":prod.price,"category":category_list}})
		except:
			return JsonResponse({"success":False,"reason":"invalid couple of product and seller name."})