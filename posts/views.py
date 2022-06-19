from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(http_method_names=["GET", "POST"])
def homepage(request:Request):

    if request.method == "POST":
        data = request.data
        response={'message':'Hello World', 'data':data}
        return Response(data=response, status=status.HTTP_201_CREATED)

    response={'message':'Hello World'}
    return Response(data=response, status=status.HTTP_200_OK)











# from django.shortcuts import render
# from django.http import HttpRequest, HttpResponse, JsonResponse
# # Create your views here.

# def homepage(request:HttpRequest):
#     response={'message':'Hello World'}
#     return JsonResponse(data=response)
