from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from api import views
                       

router = DefaultRouter()
router.register(r'Tags', views.TagViewSet)
router.register(r'Layers', views.LayerViewSet)
router.register(r'Packages', views.PackageViewSet)
router.register(r'PdxMsa2010CensusBlockGroups', views.PdxMsa2010CensusBlockGroupsViewSet)
router.register(r'PdxMsa2010CensusTracts', views.PdxMsa2010CensusTractsViewSet)
router.register(r'PdxMsaNcdbs', views.PdxMsaNcdbViewSet)
router.register(r'ParksV20190129', views.ParksV20190129ViewSet)
router.register(r'CommunityGardensV20190122', views.CommunityGardensV20190122ViewSet)
router.register(r'Dataset045Pdxs', views.Dataset045PdxViewSet)
router.register(r'Dataset045Dcs', views.Dataset045DcViewSet)


urlpatterns = [
    url(r'^create_layer/', views.create_layer, name='create_layer'),
    url(r'^create_package/', views.create_package, name='create_package'),
    url(r'^', include(router.urls)),        
]
