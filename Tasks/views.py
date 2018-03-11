# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def tasks(request):
  return render(request, 'tasks_home.html')
