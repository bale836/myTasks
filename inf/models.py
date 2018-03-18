# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Task(models.Model):
  taskName = models.CharField('taskName', blank=False, max_length=32)
  taskDesc = models.CharField('taskDesc', blank=False, max_length=128)
  taskType = models.IntegerField('taskType', blank=False, choices=(('0', 'OneTime'), ('1', 'Period'),))

  class Meta:
    db_table = "h_t_task"
