from rest_framework import generics, status, permissions
from rest_framework.response import Response
from accounts.models import User,Profil
from rest_framework import viewsets,mixins
from djoser.views import UserViewSet
from rest_framework.views import APIView
from accounts.serializers import  UserSerializer, ProfilSerializer,ProfilSerializerList
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser,MultiPartParser,FormParser,FileUploadParser




class AccountUserViewset(UserViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)


class AccountUserViewsetList(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)



class UploadPhotoViewset(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin):
    serializer_class=ProfilSerializer
    permission_classes=[IsAuthenticated]
    queryset=Profil.objects.all()
    parser_classes = (MultiPartParser, FormParser,JSONParser)

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)
        # return user


class ProfilViewSetList(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    serializer_class=ProfilSerializerList
    permission_classes=[permissions.AllowAny,]
    queryset=Profil.objects.all()
    parser_classes = (MultiPartParser, FormParser,JSONParser)





# class LogoutAPIView(generics.GenericAPIView):
#     serializer_class = LogoutSerializer

#     permission_classes = (permissions.IsAuthenticated,)

#     def post(self, request):

#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(status=status.HTTP_204_NO_CONTENT)