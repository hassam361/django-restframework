from django.shortcuts import render
from django.http import HttpResponse, JsonResponse  
from rest_framework.parsers import JSONParser
from .models import Demand 
from .serializers import DemandSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins 
from rest_framework.authentication import SessionAuthentication , BasicAuthentication
from rest_framework.permissions import IsAuthenticated 
from rest_framework import viewsets 
from django.shortcuts import get_object_or_404
class DemandViewSet(viewsets.ViewSet):
    def list(self, request):
        demand=Demand.objects.all()
        serializer= DemandSerializer(demand, many=True)
        return Response(serializer.data)
    def create(self, request):
        serializer =DemandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self, request, pk=None):
        queryset= Demand.objects.all()
        demand= get_object_or_404(queryset, pk=pk)
        serializer= DemandSerializer(demand)
        return Response(serializer.data)
    def update(self, request, pk=None):
        demand= Demand.objects.get(pk=pk)
        serializer= DemandSerializer(demand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DemandModelViewSet(viewsets.ModelViewSet):
   queryset=Demand.objects.all()
   serializer_class = DemandSerializer
   









class GenericApiView(generics.GenericAPIView,mixins.ListModelMixin):
    serializer_class=DemandSerializer
    queryset = Demand.objects.all()




# Create your views here.
class DemandApiView(APIView):
    #authentication_classes=[SessionAuthentication,BasicAuthentication]
    #permission_classes = [IsAuthenticated]
    def get(self,request):
        demand=Demand.objects.all()
        serializer= DemandSerializer(demand, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = DemandSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  


class demand_detail(APIView):
    #authentication_classes=[SessionAuthentication,BasicAuthentication]
    #permission_classes = [IsAuthenticated]
    def get(self,request, id):
        try:
            demand=Demand.objects.get(id=id)
            serializer= DemandSerializer(demand)
            return Response(serializer.data)
           
        except Demand.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
         
    def put(self,request,id):
        
        try:
            demand=Demand.objects.get(id=id)
            serializer= DemandSerializer(demand,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else: 
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  
           
        except Demand.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    def delete(self,request,id):
        try:
            demand=Demand.objects.get(id=id)
            demand.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
           
        except Demand.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
         
        
    
'''
@csrf_exempt
def demand_list(request):
    if request.method == 'GET':
        demand=Demand.objects.all()
        serializer= DemandSerializer(demand, many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == 'POST': 
        data = JSONParser().parse(request)
        serializer = DemandSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        else: 
            return serializer.errors(serializer.errors,status=400)


'''
@api_view(['GET','POST'])
def demand_list(request):   
    if request.method == 'GET':
        demand=Demand.objects.all()
        serializer= DemandSerializer(demand, many=True)
        return Response(serializer.data)
    elif request.method == 'POST': 
        
        serializer = DemandSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  