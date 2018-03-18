# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from models import Task
import json

# Create your views here.

# Initial the result message
result = {}
result['ResCode'] = "000"
result['Desc'] = "Success"

# Common method to check the request format
def chkRequestJson(request):
    reqFormat = request.META['CONTENT_TYPE']
    print "Content-Type: " + reqFormat
    if reqFormat != "application/json":
        result['ResCode'] = "-1"
        result['Desc'] = "The Content-Type is not application/json"
        return result
    
    try:
        json.loads(request.body)
    except:
        result['ResCode'] = "-1"
        result['Desc'] = "The request format is not json."
        return result

# create Task
def createTask(request):
  chkRequestJson(request)
  reqTaskBody = json.loads(request.body)
  print reqTaskBody
  _taskName = reqTaskBody['taskName']
  _taskDesc = reqTaskBody['taskDesc']
  _taskType = reqTaskBody['taskType']

  myTask = Task(taskName=_taskName, taskDesc=_taskDesc, taskType=_taskType)
  myTask.save()
  return HttpResponse(json.dumps(result), content_type="application/json")
