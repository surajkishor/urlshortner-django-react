from django.shortcuts import get_object_or_404,redirect
from rest_framework.views import APIView
from rest_framework import status
from .serializers import URLSerializer
from .models import URL
from rest_framework.response import Response
import string
import random

def generate_url():
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for _ in range(6))
    return short_code

class shorten_url(APIView):
    def post(self, request):
        data = request.data.get("original_url")
        if not data:
            return Response({"error": "original_url is required"}, status=status.HTTP_400_BAD_REQUEST)
        short_url = generate_url()

        while URL.objects.filter(short_url=short_url).exists():
            short_url = generate_url()

        url = URL.objects.create(original_url=data, short_url=short_url)
        serializer = URLSerializer(url)
        return Response({"data":serializer.data, "short_link": f"http://127.0.0.1:8000/{short_url}"}, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class redirect_url(APIView):
    def get(self, request, short_code):
        print(f"Received short code: {short_code}")
        url_object = get_object_or_404(URL, short_url=short_code)
        return redirect(url_object.original_url)
        # return Response({'original_url': url_object.original_url})