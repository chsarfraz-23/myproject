from django.urls import include, path
from rest_framework import routers

from myapp import views
from myapp.views import UserViewSet, ProductTypesViewSet, UserPostViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'ProductType', ProductTypesViewSet)
router.register(r'post-user', UserPostViewSet, basename='post-user')

urlpatterns = [
    path('', include(router.urls)),

]