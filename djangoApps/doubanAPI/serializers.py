#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @contact: voidqueens@hotmail.com
# @software: PyCharm
# @time: 2019/11/5 下午7:29
# @site: www.gongyanli.com
# @file: serializers.py
from rest_framework import serializers
from .models import UserProfile, Book


class BookSerializer(serializers.Serializer):
    '''
    使用Serializer进行序列化
    '''
    title = serializers.CharField(required=True, max_length=100)
    isbn = serializers.CharField(required=True, max_length=100)
    author = serializers.CharField(required=True, max_length=100)
    publish = serializers.CharField(required=True, max_length=100)
    rate = serializers.FloatField(default=0)


class BookModelSerializer(serializers.ModelSerializer):
    '''
    使用ModelSerializer进行序列化
    '''

    class Meta:
        model = Book
        fields = '__all__'  # 将表中所有字段进行序列化
