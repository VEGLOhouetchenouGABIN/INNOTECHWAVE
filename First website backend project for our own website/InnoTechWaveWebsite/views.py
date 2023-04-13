
from .models import Projects,DomainWork,SubscribeWebsite,OurServices
from .serializers import ProjectsSerializer,ProjectsSerializerList,DomainWorkSerializer,DomainWorkSerializerList,SubscribeWebsiteSerializer,SubscribeWebsiteSerializerList,OurServicesSerializer,OurServicesSerializerList
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework import viewsets,mixins
from djoser.views import UserViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser,MultiPartParser,FormParser,FileUploadParser


class ProjectsViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=ProjectsSerializer
    queryset=Projects.objects.all()
    permission_classes=[IsAuthenticated]
    # parser_classes = (MultiPartParser, FormParser,FileUploadParser,JSONParser)
    def perform_create(self, serializer):
        
        serializer.save(addBy=self.request.user)
        


class ProjectsViewSetList(viewsets.GenericViewSet,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    serializer_class=ProjectsSerializerList
    queryset=Projects.objects.all()
    permission_classes=[permissions.AllowAny]
    # parser_classes = (MultiPartParser, FormParser,FileUploadParser,JSONParser)

class DomainWorkViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=DomainWorkSerializer
    queryset=DomainWork.objects.all()
    permission_classes=[IsAuthenticated]
    # parser_classes = (MultiPartParser, FormParser,FileUploadParser,JSONParser)
    def perform_create(self, serializer):
        
        serializer.save(createBy=self.request.user)
        


class DomainWorkViewSetList(viewsets.GenericViewSet,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    serializer_class=DomainWorkSerializerList
    queryset=DomainWork.objects.all()
    permission_classes=[permissions.AllowAny]
    # parser_classes = (MultiPartParser, FormParser,FileUploadParser,JSONParser)


class OurServicesViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=OurServicesSerializer
    queryset=OurServices.objects.all()
    permission_classes=[IsAuthenticated]
    # parser_classes = (MultiPartParser, FormParser,FileUploadParser,JSONParser)
    def perform_create(self, serializer):
        
        serializer.save(addBy=self.request.user)
        


class OurServicesViewSetList(viewsets.GenericViewSet,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    serializer_class=OurServicesSerializerList
    queryset=OurServices.objects.all()
    permission_classes=[permissions.AllowAny]
    # parser_classes = (MultiPartParser, FormParser,FileUploadParser,JSONParser)


class SubscribeWebsiteViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=SubscribeWebsiteSerializer
    queryset=SubscribeWebsite.objects.all()
    permission_classes=[IsAuthenticated]
    # parser_classes = (MultiPartParser, FormParser,FileUploadParser,JSONParser)
    def perform_create(self, serializer):
        serializer.save()
        


class SubscribeWebsiteViewSetList(viewsets.GenericViewSet,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    serializer_class=SubscribeWebsiteSerializerList
    queryset=SubscribeWebsite.objects.all()
    permission_classes=[permissions.AllowAny]
    # parser_classes = (MultiPartParser, FormParser,FileUploadParser,JSONParser)

