from django.shortcuts import render
import uuid

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from backend_api.models import Product
from backend_api.serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework import response, decorators, permissions, status

import base64
from django.core.files.base import ContentFile


@api_view(['GET', 'POST', 'DELETE'])
# @decorators.permission_classes([permissions.IsAuthenticated])
def product(request):
    if request.method == 'GET':
        products = Product.objects.all()
        products_serializer = ProductSerializer(products, many=True)
        return JsonResponse(products_serializer.data, safe=False)
    elif request.method == 'POST':
        # product_data = JSONParser().parse(request)
        product_data = request.data
        product_data['product_auction_status'] = 0
        products_total = Product.objects.all()
        # create product_code
        if products_total:
            product_latest = products_total.order_by("-id")[0]
            product_data['product_code'] = f"VNA{(product_latest.id + 1):07d}"
        else:
            product_data['product_code'] = f"VNA{1:07d}"
        #  add product_image
        if product_data['product_images']:
            data_image_base64 = product_data['product_images'][0]['path']
            format, imgstr = data_image_base64.split(';base64,')
            ext = format.split('/')[-1]

            data_image = ContentFile(base64.b64decode(imgstr), name=(str(uuid.uuid4()) + '.' + ext))
            product_data['product_image_1'] = data_image
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
