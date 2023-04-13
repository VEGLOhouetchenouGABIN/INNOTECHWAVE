from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import AccountUserViewset , UploadPhotoViewset,ProfilViewSetList,AccountUserViewsetList

router = DefaultRouter()
router.register('user', AccountUserViewset,basename='user')
router.register('users', AccountUserViewsetList,basename='users')
router.register('photo', UploadPhotoViewset,basename='photo')
router.register('photos', ProfilViewSetList,basename='photos')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.jwt')),
]