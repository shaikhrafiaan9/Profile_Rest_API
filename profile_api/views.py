from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HelloSerializer
from rest_framework import status

# Create your views here.

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
