from django.db.models import fields
from .models import *
from rest_framework import serializers

class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=ServiceCategory
        exclude=['created_at','updated_at']

class ServiceSubCategorySerializer(serializers.ModelSerializer):
    services=ServiceCategorySerializer()
    class Meta:
        model=ServiceSubCategory
        fields=['id','sub_service_name','logo','services']
        
class ServiceBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=ServiceBooking
        fields=['sub_services','id','name','mobile_number','date',
                'time','type','problem','flat','zip_code']
