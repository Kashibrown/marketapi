from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MarketSerializer
from .models import *

@api_view(['GET']) #overview of the urls in my api
def api_overview(request):
    
    api_urls = {
        'List' : '/market-list/',
        'Create': '/market-create',
        'Update' : '/market-update/<str:pk>/',
        'Delete' : '/market-delete',
        'Detail View' : '/market-detail/<str:pk>/'
    }
    return Response(api_urls)  


@api_view(['GET'])
def marketList(request):
    market = Market.objects.all() #quering my database
    serializer = MarketSerializer(market, many=True) #this would take care of serializing the market data
    
    return Response(serializer.data)

@api_view(['GET'])
def marketDetail(request, pk): #we passed in the primary key here so as to get the particular object
    market = Market.objects.get(id = pk)
    serializer = MarketSerializer(market, many= False) #many= false because we want it to return one object, we are getting the object one by one
    
    return Response(serializer.data) 

@api_view(['POST']) #we are creating/adding  to our database  
def marketCreate(request):
    serializer = MarketSerializer(data= request.data) #basically this sends us some object
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED) 
    return Response (serializer.errors , status = status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def marketUpdate(request, pk):
    market = Market.objects.get(id = pk)
    serializer = MarketSerializer(instance=market, data=request.data)#the instance is set to that because we are update the item that's in the market 
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def marketDelete(request, pk):
    market= Market.objects.get(id = pk)
    market.delete()
    
    return Response('Deleted Successfully')