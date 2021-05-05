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
        if request.query_params.get('size', None):
            size = request.query_params.get('size', None)
            products = Product.objects.order_by('-created_time')[:int(size)]
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
        #  create product_image
        if 'product_images' in product_data and product_data['product_images']:
            for n in range(len(product_data['product_images'])):
                data_image_base64 = product_data['product_images'][n]['path']
                format, imgstr = data_image_base64.split(';base64,')
                ext = format.split('/')[-1]
                data_image_file = ContentFile(base64.b64decode(imgstr),
                                              name=(product_data['product_code'] + '_' + str(uuid.uuid4()) + '.' + ext))
                field_idx = f"product_image_{str(n + 1)}"
                product_data[field_idx] = data_image_file
        # create product_owner_represent_id_card_image front + back:
        for field in ['product_owner_represent_id_card_image_front', 'product_owner_represent_id_card_image_back']:
            if field in product_data and product_data[field]:
                data_image_base64 = product_data[field][0]['path']
                format, imgstr = data_image_base64.split(';base64,')
                ext = format.split('/')[-1]
                data_image_file = ContentFile(base64.b64decode(imgstr),
                                              name=(product_data['product_code'] + '_' + str(uuid.uuid4()) + '.' + ext))
                product_data[field] = data_image_file

        product_serializer = ProductSerializer(data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse(product_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
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
