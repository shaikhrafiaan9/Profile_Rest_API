from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HelloSerializer , UserProfileSerializer
from rest_framework import status
from rest_framework import viewsets
from .models import UserProfile
from rest_framework.authentication import TokenAuthentication
from .permissions import UpdateOwnProfile
from rest_framework import filters

# Create your views here.
#APIView has function that support HTTP method
#ViewSet has function that ull be performing action like list, create , update AuthenticationMiddleware

class HelloAPIView(APIView):

    serializer_class = HelloSerializer

    def get(self,request,format=None):

        an_apiview = [
        'Uses HTTP method as function (get,post,put,patch,delete)',
        'Is Similar to a Traditional Django Views',
        'Give you most control over application logics',
        'Is mapped manually to URLS'
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})

    def post(self,request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Helllo {name}'
            return Response({'message':message})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def put(self,request,pk=None):
        """ Update all the Object provided in the Request """

        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """ Update only the fields that are in the Request """
        return Response({'method':'Patch'})

    def delete(self,request,pk=None):
        """ Delete the object """
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):

    serializer_class = HelloSerializer

    def list(slef,request):
        """ Return a hello message """

        an_apiview = [
            'Uses action (list,create,update,partial_update,retrieve)',
            'Automatically maps to URLs using ROUTERS',
            'Provide more functionality with less code',
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})


    def create(self,request):

        serializer = self.serializer_class(data=serializer.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        return Response(message.errors,status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self,request,pk=None):
        """ Handle getting an pbject by its ID """
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """ handle updating an object """
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """Handle updating part of object """
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        return Response({'http_method':'DELETE'})




class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset =  UserProfile.objects.all()
    print(queryset)
    authentication_classes = (TokenAuthentication,)    #how the user will authenticate
    permission_classes = (UpdateOwnProfile,)           #how the user get permissions
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)
