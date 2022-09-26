from rest_framework import serializers
from .models import *

class MarketSerializer(serializers.ModelSerializer): #we can use any type of serializer but we want to work with a model serializer thats why the modelserializer is used here
    
    class Meta:
        model = Market
        fields = '__all__'
        