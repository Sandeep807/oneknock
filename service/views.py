from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import *
from .models import *
# Create your views here.

class ServiceView(APIView):
    def get(self,request):
        try:
            id=request.GET.get('id')
            if id is not None:
                obj=ServiceCategory.objects.filter(id=id).first()
                if obj is not None:
                    serializer=ServiceCategorySerializer(obj)
                    return Response(data=serializer.data,status=status.HTTP_200_OK)
                else:
                    return Response({'message':'Id not found'},status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'message':'Id is blank'},status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'message':'Something went wrong'},status=status.HTTP_400_BAD_REQUEST)


class ServiceSubCategoryView(APIView):
    def get(self,request):
        try:
            id=request.GET.get('id')
            if id is not None:
                obj=ServiceSubCategory.objects.filter(id=id).first()
                if obj is not None:
                    serializer=ServiceSubCategorySerializer(obj)
                    return Response(data=serializer.data,status=status.HTTP_200_OK)
                else:
                    return Response({'message':'Id not found'},status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'message':'Id is blank'},status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            print(e)
            return Response({'message':'Something went wrong'},status=status.HTTP_400_BAD_REQUEST)

class BookingServiceView(APIView):
    def post(self,request):
        try:
            data=request.data
            serializer=ServiceBookingSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(data=serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            print(e)
            return Response({'message':'Something went wrong'},status=status.HTTP_400_BAD_REQUEST)