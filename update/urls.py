from django.conf.urls import url
from .views import update_model_detail_view, SerializedDetailView, SerializedListView
urlpatterns = [
    url(r'^test/$', update_model_detail_view, name='test'),
    url(r'^list/$', SerializedListView.as_view(), name='detail'),
    url(r'^detail/$', SerializedDetailView.as_view(), name='list'),
]