from rest_framework import serializers
from .models import *
import string
import random
from django.db import IntegrityError
from icecream import ic

class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ["original_url","short_url"]
        read_only_fields = ['short_url']
        

    def create(self, validated_data):
        org_url = validated_data
        sh_url = self.generate_url()

        while URL.objects.filter(short_url=sh_url).exists():
            sh_url = self.generate_url()
        
        url = URL.objects.create(**validated_data, short_url=sh_url)
        return url

    def generate_url(self):
        characters = string.ascii_letters + string.digits
        short_code = ''.join(random.choice(characters) for _ in range(6))

        return short_code

# class ShortURLserializer(serializers.ModelSerializer):
#     class Meta:
#         model = URL
#         feilds = ['short_url']