# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Host(models.Model):
	ip = models.CharField(max_length=150)
	status = models.TextField(blank=True)
	accessed = models.IntegerField(blank=True,null=True,default=0)
	command = models.TextField(blank=True)
	def __str__(self):
		return self.ip

# Create your models here.