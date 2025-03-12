from django.shortcuts import render
from django.http import JsonResponse
import json

def api_home(request, *args, **kwargs):
    data1 = {
        "name": "John Doe",
        "age": 23,
        "is_student": True
    }

    try:
        data = json.loads(request.body.decode('utf-8'))
    except json.JSONDecodeError:
        data = {}

    print('>>>>>>', data)
    data = data1
    return JsonResponse(data)
