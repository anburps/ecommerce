from rest_framework import serializers

from app.models import Product



class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product     
        fields = ["id","name","description","category","slug","inventory","old_price","price"]