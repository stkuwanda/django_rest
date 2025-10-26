from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer

 
@api_view(['GET'])
def get_users(request): 
  users = User.objects.all()[:10] # retrieve 10 users
  serializer = UserSerializer(users, many=True) # serialize the users which can be a list (many=true)
  return Response(serializer.data) # return serialized data
 
@api_view(['POST'])
def create_user(request): 
  serializer = UserSerializer(data=request.data) # create a UserSerializer instance with the data from the request
  if serializer.is_valid(): # check if the data is valid
    serializer.save() # save the new user to the database
    return Response(serializer.data, status=status.HTTP_201_CREATED) # return the serialized data with a 201 status code
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # return the errors with a 400 status code

@api_view(['GET','PUT','DELETE'])
def user_detail(request, pk):
  try:
    user = User.objects.get(pk=pk) # retrieve the user by primary key
  except User.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND) # return 404 if user not found
  if request.method == 'GET':
    serializer = UserSerializer(user) # serialize the user
    return Response(serializer.data) # return the serialized data
  elif request.method == 'PUT':
    serializer = UserSerializer(user, data=request.data) # create a UserSerializer instance with the existing user and the new data
    if serializer.is_valid(): # check if the new daata is valid
      serializer.save() # save the updated user to the database
      return Response(serializer.data) # return the serialized data
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # return the errors with a 400 status code
  elif request.method == 'DELETE':
    user.delete() # delete the user from the database
    return Response(status=status.HTTP_204_NO_CONTENT) # return 204 status code indicating successful deletion