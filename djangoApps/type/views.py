from django.shortcuts import render
from .serializers import TypeModelSerializer, Type1ModelSerializer, Type2ModelSerializer, Type3ModelSerializer, \
    Type4ModelSerializer
from .models import Type, Type1, Type2, Type3, Type4
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer


class TypeView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        Types = Type.objects.all()
        Types_serializer = TypeModelSerializer(Types, many=True)
        return Response(Types_serializer.data)

    def post(self, request):
        name = request.data.get('name')
        category_type = request.data.get('lei')
        parent_category_id = request.data.get('parent')
        type = Type()
        type.name = name
        type.category_type = category_type
        type.parent_category_id = parent_category_id
        # if parent_category_id:
        #     parent_category = Type.objects.filter(id=parent_category_id).first()
        #     type.parent_category = parent_category
        type.save()
        type_serializer = TypeModelSerializer(type)
        return Response(type_serializer.data)


class Type1View(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        Types = Type1.objects.all()
        Types_serializer = Type1ModelSerializer(Types, many=True)
        return Response(Types_serializer.data)


class Type2View(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        Types = Type2.objects.all()
        Types_serializer = Type1ModelSerializer(Types, many=True)
        return Response(Types_serializer.data)


class Type3View(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        Types = Type3.objects.all()
        Types_serializer = Type1ModelSerializer(Types, many=True)
        return Response(Types_serializer.data)


class Type4View(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        Types = Type4.objects.all()
        Types_serializer = Type1ModelSerializer(Types, many=True)
        return Response(Types_serializer.data)
