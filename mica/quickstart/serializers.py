from django.contrib.auth.models import user 
from rest_framework import serializers
from models import user
class serializeruser(serializers.ModelSerializer):
    class Meta:
        models=user
        fields=["username","lastname","age",]
