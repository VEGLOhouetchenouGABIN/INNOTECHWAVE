from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ProjectsViewSet,ProjectsViewSetList,DomainWorkViewSet,DomainWorkViewSetList,OurServicesViewSet,OurServicesViewSetList,SubscribeWebsiteViewSet,SubscribeWebsiteViewSetList

router = DefaultRouter()
router.register('project', ProjectsViewSet,basename='project')
router.register('projects', ProjectsViewSetList,basename='projects')
router.register('domainwork', DomainWorkViewSet,basename='domainwork')
router.register('domainworks', DomainWorkViewSetList,basename='domainworks')
router.register('ourservice', OurServicesViewSet,basename='ourservice')
router.register('ourservices', OurServicesViewSetList,basename='ourservices')
router.register('subscribe', SubscribeWebsiteViewSet,basename='subscribe')
router.register('subscribes', SubscribeWebsiteViewSetList,basename='subscribes')

urlpatterns = [
    path('', include(router.urls)),
]