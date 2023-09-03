from .models import Drink
from .serializer import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def get_drinks(request):

  if request.method == 'GET':
    drinks = Drink.objects.all()
    serializer = DrinkSerializer(drinks, many=True)
    return Response({'drinks' : serializer.data}, status=status.HTTP_200_OK)

  elif request.method == 'POST':
    serializer = DrinkSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'message': 'Drink Created Successfully!', 'drink': serializer.data}, status=status.HTTP_201_CREATED)
    

@api_view(['GET', 'PUT', 'DELETE'])
def drink_details(request, id):

  try:
    drink = Drink.objects.get(pk=id)
  except Drink.DoesNotExist:
    return Response({'message': 'Drink not found'},status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = DrinkSerializer(drink)
    return Response({'drink' : serializer.data}, status=status.HTTP_200_OK)

  elif request.method == 'PUT':
    serializer = DrinkSerializer(drink, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'message': 'Drink Updated Successfully!', 'drink': serializer.data}, status=status.HTTP_201_CREATED)

  elif request.method == 'DELETE':
    drink.delete()
    return Response({'message' : 'Drink Deleted Successfully'}, status=status.HTTP_204_NO_CONTENT)
