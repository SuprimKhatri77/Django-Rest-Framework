from rest_framework import serializers
from .models import *


class QuoteSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    class Meta:
        model = Quote
        fields = ['id','quote','time_stamp','author']