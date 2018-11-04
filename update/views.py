from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Update
from django.views import View
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


class SerializedDetailView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        print('jajajaja')
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type='application/json')


class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        qs = Update.objects.all()
        #data = serialize('json', qs, fields=('user', 'content'))
        #print data
        #json_data = data
        json_data = Update.objects.all().serialize()
        #data = {
        #    "user": obj.user.username,
        #    "content":obj.content
        #}
        return HttpResponse(json_data, content_type='application/json')
