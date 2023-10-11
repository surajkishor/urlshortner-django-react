from rest_framework import serializers
from .models import *

class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        feilds =' __all__'


        # def create(self, data):
        #     org_url = data('original_url')
        #     sh_url = self.context("short_url")

        #     url = URL.objects.create(original_url=org_url,short_url=sh_url)
        #     url.save()

# class ShortURLserializer(serializers.ModelSerializer):
#     class Meta:
#         model = URL
#         feilds = ['short_url']