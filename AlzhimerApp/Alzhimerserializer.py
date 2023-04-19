from rest_framework import serializers
from .models import Alzhimer

class alzhimerSerializers(serializers.ModelSerializer):

    class Meta:
        model= Alzhimer
        fields='__all__'