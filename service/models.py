from django.db import models

# Create your models here.
def generate_id():
    try:
        obj=ServiceCategory.objects.all().last()
        if obj is not None:
            return (obj.id)+1
        else:
            return 1001
    except Exception as e:
        print(e)
class ServiceCategory(models.Model):
    id=models.IntegerField(default=generate_id,primary_key=True,editable=False)
    service_name=models.CharField(max_length=100)
    logo=models.ImageField(upload_to='service/logo/')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.service_name

def generate_id():
    try:
        obj=ServiceSubCategory.objects.all().last()
        if obj is not None:
            return (obj.id)+1
        else:
            return 1001
    except Exception as e:
        print(e)

class ServiceSubCategory(models.Model):
    id=models.IntegerField(default=generate_id,primary_key=True,editable=False)
    sub_service_name=models.CharField(max_length=100)
    logo=models.ImageField(upload_to='sub_service/logo/')
    services=models.ForeignKey(ServiceCategory,related_name='service',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.sub_service_name

def generate_id():
    try:
        obj=ServiceBooking.objects.all().last()
        if obj is not None:
            return (obj.id)+1
        else:
            return 1001
    except Exception as e:
        print(e)

class ServiceBooking(models.Model):
    sub_services=models.ForeignKey(ServiceSubCategory,on_delete=models.CASCADE)
    id=models.IntegerField(default=generate_id,primary_key=True,editable=True)
    name=models.CharField(max_length=100)
    mobile_number=models.CharField(max_length=100)
    date=models.DateField()
    time=models.TimeField()
    type=models.CharField(max_length=100,null=True,blank=True)
    problem=models.TextField()
    flat=models.TextField()
    zip_code=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.sub_service_name


