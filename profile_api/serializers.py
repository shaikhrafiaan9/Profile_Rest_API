from rest_framework import serializers
from .models import UserProfile
#from profile_api import models



class HelloSerializer(serializers.Serializer):
    name =  serializers.CharField(max_length=10)



class UserProfileSerializer(serializers.ModelSerializer):     #we will be overwirying defaulf create method as it uses defaulf objects to create
    """ Serialize a user profile object """
    class Meta:
        model = UserProfile
        fields = ('id','email','name','password')
        extra_kwargs = {
            'password' : {
                'write_only':True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self,validated_data):
        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

    def update(self,instance,validated_data):
        """Handle updating user account"""
        if password in validated_data:
            password=validated_data.pop('password')
            instance.set_password('password')

        return super().update(instance,validated_data)
