from .models import Product
from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import ProductSerializer
from rest_framework import generics

class DetailProductView(generics.RetrieveAPIView):
    queryset =Product.objects.all()
    serializer_class=ProductSerializer

class CreateProductView(generics.CreateAPIView):
    queryset =Product.objects.all()
    serializer_class=ProductSerializer
    def perform_create(self, serializer):
        name=serializer.validated_data.get('name')
        content=serializer.validated_data.get('content') or None
        if content is None:
            content=name
        serializer.save(content=content)

class UdapteProductView(generics.UpdateAPIView):
    queryset =Product.objects.all()
    serializer_class=ProductSerializer
    def perform_update(self, serializer):
        name=serializer.validated_data.get('name')
        content=serializer.validated_data.get('content') or None
        if content is None:
            content=name
        serializer.save(content=content)







































# @api_view(['POST'])
# def view_api(request):
#     # query= Product.objects.all().order_by('?').first()
#         # data = model_to_dict(query, fields=('name', 'content'))
#         #serealization:mettre les donees sous forme de dictionnnaire
#     serializer=ProductSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response({'Details':'invalid data'})
#     # data=request.data    
#     # return Response(data)
