from rest_framework import serializers
from myapp.models import User, ProductTypes


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTypes
        fields = '__all__'