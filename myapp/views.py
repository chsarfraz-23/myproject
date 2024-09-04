from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, \
    CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from myapp.models import ProductTypes, User
from myapp.serializers import ProductTypeSerializer, UserSerializer


class UserPostViewSet(CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserViewSet(ListModelMixin,
                  RetrieveModelMixin,
                  UpdateModelMixin,
                  DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class ProductTypesViewSet(viewsets.ModelViewSet):
    queryset = ProductTypes.objects.all()
    serializer_class = ProductTypeSerializer
    permission_classes = [IsAuthenticated]
