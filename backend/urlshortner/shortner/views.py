from django.shortcuts import get_object_or_404,redirect
from rest_framework.views import APIView
from rest_framework import status
from .serializers import URLSerializer
from .models import URL
from rest_framework.response import Response
import string
import random
from icecream import ic



class shorten_url(APIView):
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = URLSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            short_url = serializer.save()
            ic()
            response = {
                "original_url":short_url.original_url,
                "short_urll": f'http://localhost:8000/{short_url.short_url}'
            }
            return Response({"response":response}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class redirect_url(APIView):
    def get(self, request, short_code):
        url_object = get_object_or_404(URL, short_url=short_code)
        return redirect(url_object.original_url)
        # return Response({'original_url': url_object.original_url})