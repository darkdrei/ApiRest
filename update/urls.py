from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^test/$', update_model_detail_view, name='test'),
    url(r'^list/$', SerializedListView.as_view(), name='detail'),
    url(r'^detail/$', SerializedDetailView.as_view(), name='list'),
    url(r'^detail2/$', update_model_detail_view2, name='details2'),
    url(r'^json/cbv/$', JsonCBV.as_view(), name='cbv'),
    url(r'^json/cbv2/$', JsonCBV2.as_view(), name='cbv'),
]