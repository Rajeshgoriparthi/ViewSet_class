from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ViewSet
from app.models import *
from app.serializers import *
from rest_framework.response import Response

class ProdutCrud(ViewSet):
    def list(self,request):
        PQO=Product.objects.all()
        PSD=Productserializers(PQO,many=True)
        return Response(PSD.data)

    
    def create(self,request):
        PSD=Productserializers(data=request.data)
        if PSD.is_valid():
            PSD.save()
            return Response({'success':'Product is created....!'})
        else:
            return Response({'faild':'Product created Faild...!'})
        
        
    def retrieve(self,request,pk):
        PSO=Product.objects.get(pk=pk)
        PSD=Productserializers(PSO)
        return Response(PSD.data)
    
    
    def update(self,request,pk):
        PQO=Product.objects.get(pk=pk)
        PSD=Productserializers(PQO,data=request.data)
        if PSD.is_valid():
            PSD.save()
            return Response({'success':'Product is updated....!'})
        else:
            return Response({'success':'Product is not updated....!'})
        
        
    def partial_update(self,request,pk):
        PQO=Product.objects.get(pk=pk)
        PSD=Productserializers(PQO,data=request.data,partial=True)
        if PSD.is_valid():
            PSD.save()
            return Response({'success':'Product is parcial updated....!'})
        else:
            return Response({'success':'Product is parcial not updated....!'})
        
        
    def destroy(self,request,pk):
        Product.objects.get(pk=pk).delete()
        return Response({'dalete':'Product is deleted...!'})