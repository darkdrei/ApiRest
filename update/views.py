from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Update
# Create your views here.
"""
def detail_view(request):
    return JsonResponse
"""

def update_model_detail_view(request):
    data = {
        "count": 1000,
        "content": "Some new content"
    }
    return JsonResponse(data)
