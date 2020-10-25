from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloAPIView(APIView):

    def get(self,request,format=None):

        an_apiview = [
        'Uses HTTP method as function (get,post,put,patch,delete)',
        'Is Similar to a Traditional Django Views',
        'Give you most control over application logics',
        'Is mapped manually to URLS'
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})
