from django.urls import path , include
from . import views
from rest_framework.routers import DefaultRouter


#ROUTERS is a class provided by DRF in order to generate different route that are availabel to our ViewSet.

router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,basename='hello-viewset')
router.register('profile',views.UserProfileViewSet)


urlpatterns = [

    path('hello-view/',views.HelloAPIView.as_view()),
    path('',include(router.urls))

]
