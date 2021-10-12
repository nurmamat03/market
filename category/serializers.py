from rest_framework import serializers
from .models import Category


class CategorySerializers(serializers.ModelSerializers):
    class Meta:
        model = Category
        fields = ('id', 'title', 'slug')

