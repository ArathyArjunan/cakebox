from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from cake_api.serializers import Userserializer,CakeSerializer

from cakeapp.models import User,Cakes


class Userview(APIView):
    def post(self,request,*args, **kwargs):
     serializer=Userserializer(data=request.data)
     if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data)
     else:
        return Response(data=serializer.errors)
     

class CakeView(ModelViewSet):
   serializer_class=CakeSerializer
   queryset=Cakes.objects.all()

