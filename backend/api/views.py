from django.shortcuts import render
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    data = {
        "name":"John Doe",
        "age": 23,
        "is_student": True
    }
    return JsonResponse(data)
