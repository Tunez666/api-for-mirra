from rest_framework import serializers
from .models import arrr

class ArrrSerializer(serializers.ModelSerializer):
    class Meta:
        model = arrr
        fields = ['id', 'token', 'key', 'title']