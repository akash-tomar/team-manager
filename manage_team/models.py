# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Member(models.Model):
	TYPE = (
		(0,'Admin'),
		(1,'Regular'),
	)
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	email = models.CharField(max_length=100)
	phone = PhoneNumberField(null=True, blank=True, help_text=('Only Indian'))
	role = models.IntegerField(choices=TYPE,default=1)