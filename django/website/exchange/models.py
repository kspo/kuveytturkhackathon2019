# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Order(models.Model):
	order_id = models.IntegerField(null=True)
	user_id = models.IntegerField(null=True)
	market = models.IntegerField(null=True)
	amount = models.IntegerField(null=True)
	price = models.IntegerField(null=True)
	submitted = models.IntegerField(null=True)
	buyOrSell = models.IntegerField(null=True)
	paymentType = models.IntegerField(null=True)
	senderSuffix = models.IntegerField(null=True)


class User(models.Model):
	user_id = models.IntegerField(null=True)
	balanceUsd = models.IntegerField(null=True)
	balanceTr = models.IntegerField(null=True)
	iban = models.CharField(max_length=100,null=True)
	name = models.CharField(max_length=50,null=True)
# Create your models here.
