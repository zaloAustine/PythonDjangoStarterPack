# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Quiz(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(verbose_name="description",null=True)
    created_date = models.DateField(auto_now=True)
    url = models.URLField(verbose_name="url",null=True)


class Question(models.Model):
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    question = models.TextField(verbose_name='question',null=False) 
    Choise1 = models.TextField(verbose_name='choice1',null=False) 
    Choise2 = models.TextField(verbose_name='choise2',null=False) 
    Choise3 = models.TextField(verbose_name='choise3',null=False) 
    Choise4 = models.TextField(verbose_name='choise4',null=False) 
    corrent_answer = models.CharField(verbose_name='correct answer',null=False,max_length=10) 



class User(models.Model):
    username = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    password = models.CharField(max_length=300)

   


