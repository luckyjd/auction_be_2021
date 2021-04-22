from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from backend_api.models import Product
from backend_api.serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework import response, decorators, permissions, status


@api_view(['GET', 'POST', 'DELETE'])
# @decorators.permission_classes([permissions.IsAuthenticated])
def product(request):
    if request.method == 'GET':
        products = Product.objects.all()
        products_serializer = ProductSerializer(products, many=True)
        return JsonResponse(products_serializer.data, safe=False)
    elif request.method == 'POST':
        product_data = JSONParser().parse(request)
        product_data['product_auction_status'] = 0
        product_serializer = ProductSerializer(data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse(product_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    # find tutorial by pk (id)
    # try:
    #     tutorial = Tutorial.objects.get(pk=pk)
    #     # GET / PUT / DELETE tutorial
    #     if request.method == 'GET':
    #         tutorial_serializer = TutorialSerializer(tutorial)
    #         return JsonResponse(tutorial_serializer.data)
    #
    #     elif request.method == 'PUT':
    #         tutorial_data = JSONParser().parse(request)
    #         tutorial_serializer = TutorialSerializer(tutorial, data=tutorial_data)
    #         if tutorial_serializer.is_valid():
    #             tutorial_serializer.save()
    #             return JsonResponse(tutorial_serializer.data)
    #         return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    #     elif request.method == 'DELETE':
    #         tutorial.delete()
    #         return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    #
    # except Tutorial.DoesNotExist:
    return JsonResponse({'message': 'The product does not exist'}, status=status.HTTP_404_NOT_FOUND)

#
# @api_view(['GET'])
# def tutorial_list_published(request):
#     # GET all published tutorials
#     tutorials = Tutorial.objects.filter(published=True)
#
#     if request.method == 'GET':
#         tutorials_serializer = TutorialSerializer(tutorials, many=True)
#         return JsonResponse(tutorials_serializer.data, safe=False)
