from django.shortcuts import render
from .models import Category
from .serializers import CategorySerializers
from rest_framework import permissions
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateDestroyAPIView,
)


class CategoryListView(ListAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]


class CategoryCreateView(CreateAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]


class CategoryUpdateView(RetrieveUpdateAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]


class CategoryDeleteView(RetrieveDestroyAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]

class CategoryDetail(RetrieveUpdateAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]
