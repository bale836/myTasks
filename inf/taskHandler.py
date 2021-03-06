# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from models import Task
import json
import datetime

# Create your views here.

# Initial the result message
def initResMsg():
  result = {}
  result['code'] = "000"
  result['msg'] = "Success"
  return result

# Common method to check the request format
def chkRequestJson(request):
    reqFormat = request.META['CONTENT_TYPE']
    print "Content-Type: " + reqFormat
    if reqFormat != "application/json":
        result['code'] = "-1"
        result['msg'] = "The Content-Type is not application/json"
        return result
    
    try:
        json.loads(request.body)
    except:
        result['code'] = "-1"
        result['msg'] = "The request format is not json."
        return result

# create Task
def dispatcherMsg(request):
  ## 反射机制  
  pass

def createTask(request):
  result = initResMsg()
  chkRequestJson(request)
  reqTaskBody = json.loads(request.body)
  print reqTaskBody
  _taskName = reqTaskBody['taskName']
  _taskDesc = reqTaskBody['taskDesc']
  _taskType = reqTaskBody['taskType']

  myTask = Task(taskName=_taskName, taskDesc=_taskDesc, taskType=_taskType)
  myTask.save()
  return HttpResponse(json.dumps(result), content_type="application/json")

# query Tasks
def queryTask(request):
  result = initResMsg()
  chkRequestJson(request)
  print "body: " + request.body
  reqTaskBody = json.loads(request.body)
  
  if reqTaskBody.has_key('startCreateTime'):
    _startCreateTime = datetime.datetime.strptime(reqTaskBody['startCreateTime'], "%Y-%m-%d")
    _endCreateTime = datetime.datetime.strptime(reqTaskBody['endCreateTime'], "%Y-%m-%d")
    _endCreateTime = _endCreateTime + datetime.timedelta(days=1)
    
    #tasks = Task.objects.filter(createTime__range=(_startCreateTime, _endCreateTime)).values('id', 'taskName', 'taskDesc', 'createTime')
    tasks = Task.objects.filter(createTime__range=(_startCreateTime, _endCreateTime)).values()
 
  result['data'] = list(tasks)
  return JsonResponse(result)
