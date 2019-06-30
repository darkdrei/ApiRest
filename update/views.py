from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Update
from django.views import View
import json
from Api.mixin import JsonResponseMixin
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

def update_model_detail_view2(request):
    data = {
        "count": 1000,
        "content": "Some new content"
    }
    json_data= json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')


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
        json_data = Update.objects.filter(user__id=1).serialize('Esto es desde la vista')
        #data = {
        #    "user": obj.user.username,
        #    "content":obj.content
        #}
        return HttpResponse(json_data, content_type='application/json')


class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some new content"
        }
        return JsonResponse(data)


class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some new content"
        }
        return self.render_to_json_response(data)

class UpdateModelDetailApiView():
    def get(self, request, *args, **kwargs):
        return #json

    def post(self, request, *args, **kwargs):
        return #json



    def delete(self, request, *args, **kwargs):
        return #json


class UpdateModelChangeApiView():
    def put(self, request, *args, **kwargs):
        return #json


class UpdateModelListApiView():
    def get(self, request, *args, **kwargs):
        return   #json