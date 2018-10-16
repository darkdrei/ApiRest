from django.conf.urls import url
from .views import update_model_detail_view
urlpatterns = [
    url(r'^test/$', update_model_detail_view, name='test'),
]