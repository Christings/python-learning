from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.throttling import AnonRateThrottle
from rest_framework.response import Response


class IndexView(APIView):
    def get(self, request):
        # j = 0
        # for i in request.META:
        #     print(i, ":", request.META[i])
        #     j += 1
        # print(j, "条信息")
        throttle_classes = (AnonRateThrottle,)
        return Response('hello')
