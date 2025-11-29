from rest_framework import serializers
from .models import Users

class UserSerializer(serializers.ModelSerializer):
    class meta:
        model=Users
        fields='__all__'