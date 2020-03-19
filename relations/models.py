# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Language(models.Model):
    name = models.CharField(max_length =10)
    pass

class Framework(models.Model):
    name = models.CharField(max_length =10)
    Language = models.ForeignKey(Language,on_delete=models.CASCADE)
    pass