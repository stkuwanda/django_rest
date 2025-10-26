from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer

 
@api_view(['GET'])
def get_user(request): 
  serializer = UserSerializer({"name":"Michal-nav", "age": 0}) # create a UserSerializer instance with sample data
  return Response(serializer.data) # return the serialized data as a response