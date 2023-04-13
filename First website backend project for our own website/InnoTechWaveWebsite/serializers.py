from rest_framework.serializers import ModelSerializer
from .models import Projects,DomainWork,SubscribeWebsite,OurServices


class ProjectsSerializer(ModelSerializer):
    class Meta:
        model=Projects
        fields=['id','name','description','url','addBy','cover']

class ProjectsSerializerList(ModelSerializer):
    class Meta:
        model=Projects
        fields=['id','name','description','url','addBy','cover']
        depth=1


class DomainWorkSerializer(ModelSerializer):
    class Meta:
        model=DomainWork
        fields=['id','name','description','photo','createBy']

class DomainWorkSerializerList(ModelSerializer):
    class Meta:
        model=DomainWork
        fields=['id','name','description','photo','createBy']
        depth=1

class OurServicesSerializer(ModelSerializer):
    class Meta:
        model=OurServices
        fields=['id','name','description','addBy']

class OurServicesSerializerList(ModelSerializer):
    class Meta:
        model=OurServices
        fields=['id','name','description','addBy']
        depth=1

class SubscribeWebsiteSerializer(ModelSerializer):
    class Meta:
        model=SubscribeWebsite
        fields=['id','email']

class SubscribeWebsiteSerializerList(ModelSerializer):
    class Meta:
        model=SubscribeWebsite
        fields=['id','email']
        depth=1


