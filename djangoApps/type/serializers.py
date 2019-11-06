#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @contact: voidqueens@hotmail.com
# @software: PyCharm
# @time: 2019/11/6 下午4:00
# @site: www.gongyanli.com
# @file: serializers.py
from .models import Type, Type1, Type2, Type3, Type4
from rest_framework import serializers


class TypeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"


class Type1ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type1
        fields = "__all__"


class Type2ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type2
        fields = "__all__"


class Type3ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type3
        fields = "__all__"


class Type4ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type4
        fields = "__all__"
