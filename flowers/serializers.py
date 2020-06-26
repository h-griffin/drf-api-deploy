from rest_framework import serializers

from .models import Flower

class FlowersSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','name','planter','description','created_at')
        model = Flower

        