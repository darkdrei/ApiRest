from rest_framework import serializers
from status import models as status


class StatusSearializer(serializers.ModelSerializer):
    class Meta:
        model =  status.Status
        fields = [
            'user',
            'content',
            'image'
        ]