# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Member(models.Model):
	TYPE = (
		(0,'Admin'),
		(1,'Regular'),
	)
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	email = models.CharField(max_length=100)
	phone = models.CharField(max_length=10,null=True,blank=True)
	role = models.IntegerField(choices=TYPE,default=1)