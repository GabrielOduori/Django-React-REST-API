# Using the router from rest_framework


from rest_framework import routers
from .api import LeadViewSet

router  = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'leads') #leads is the name of the viewset


urlpatterns = router.urls