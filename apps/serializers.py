from rest_framework import serializers
from .models import *
class AppsSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = '__all__'

    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

class AppNestedSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    sub_category = SubCategorySerializer()
    class Meta:
        model = App
        fields = '__all__'