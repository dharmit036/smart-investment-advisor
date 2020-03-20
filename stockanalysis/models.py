# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class stockdata(models.Model):
    symbol=models.CharField(max_length=30)
    name=models.CharField(max_length=100)
    price=models.CharField(max_length=30)
    change=models.CharField(max_length=30)
    volume=models.CharField(max_length=30)

    def __unicode__(self):
        return str(self.name)

class userdata(models.Model):
    your_name=models.CharField(max_length=100)
    username=models.CharField(max_length=50,primary_key=True)
    email_id=models.CharField(max_length=50)
    birth_date=models.DateField()
    job_type=models.CharField(max_length=15)
    phone_no=models.CharField(max_length=15)
    income=models.CharField(max_length=100)
    plans=models.CharField(max_length=150)
    schemes=models.CharField(max_length=50)
    ex_returns=models.CharField(max_length=50)
    problems_faced=models.CharField(max_length=50)
    saving_ratio=models.CharField(max_length=20)
    span=models.CharField(max_length=30)

    def __unicode__(self):
        return "%s %s" % (self.your_name,self.username)

class extrastock(models.Model):
    symbol=models.CharField(max_length=50)
    name=models.CharField(max_length=100)
    price=models.CharField(max_length=30)
    change=models.CharField(max_length=30)

    def __unicode__(self):
        return str(self.name)

class mostloser(models.Model):
    name=models.CharField(max_length=100)
    price=models.CharField(max_length=30)
    change=models.CharField(max_length=30)

    def __unicode__(self):
        return str(self.name)

class userinfo(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    income=models.BigIntegerField()
    span=models.CharField(max_length=100)
    problem=models.CharField(max_length=100)
    ex_return=models.CharField(max_length=10)

    def __unicode__(self):
        return "%s:%s" % (self.username,self.name)

class yearlyrecom(models.Model):
    symbol=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    quantity=models.CharField(max_length=50)
    rrate=models.CharField(max_length=20)

    def __unicode__(self):
        return "%s:%s" % (self.symbol,self.name)


class monthlyrecom(models.Model):
    symbol=models.CharField(max_length=100)
    stockname=models.CharField(max_length=100)
    rrate=models.CharField(max_length=20)

    def __unicode__(self):
        return "%s:%s" % (self.symbol,self.name)