from rest_framework import serializers
from .models import User

# Serializer for the User model which converts model instances to JSON and vice versa
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__' # Serialize all fields of the User model