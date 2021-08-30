from rest_framework import serializers
from .models import Demand

from django.utils import timezone

'''
class DemandSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.TextField(max_length=500)
    date_posted = serializers.DateTimeField()
    def create(self, validated_data):
        return Demand.objects.create(validated_data)
'''
class DemandSerializer(serializers.ModelSerializer):
    class Meta: 
        model=Demand 
        fields=['id','title','description'] 