from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, APIView
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404

from posts import serializers

@api_view(http_method_names=["GET", "POST"])
def homepage(request:Request):

    if request.method == "POST":
        data = request.data
        response={'message':'Hello World', 'data':data}
        return Response(data=response, status=status.HTTP_201_CREATED)

    response={'message':'Hello World'}
    return Response(data=response, status=status.HTTP_200_OK)


class PostListCreateView(APIView):
    serializer_class = PostSerializer

    """ a view for creating and listing posts """
    def get(self, request:Request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = self.serializer_class(instance=posts, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK) 

    def post(self, request:Request, *args, **kwargs):
        data = request.data 
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message":"Post Created!",
                "data":serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED) 
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class PostRetrieveUpdateDeleteView(APIView):
    serializer_class = PostSerializer

    def get(self, request:Request, post_id:int):
        post = get_object_or_404(Post, pk=post_id)
        serializer = self.serializer_class(instance=post)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request:Request, post_id:int):
        post = get_object_or_404(Post, pk=post_id)
        data = request.data 
        serializer = self.serializer_class(instance=post, data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message":"Post Updated",
                "data":serializer.data
            }
            return Response(data=response, status=status.HTTP_200_OK) 
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request:Request, post_id:int):
        post = get_object_or_404(Post, pk=post_id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






# @api_view(http_method_names=['GET'])
# def post_detail(request:Request, post_id:int):
#     post = get_object_or_404(Post, pk=post_id)
#     serializer = PostSerializer(instance=post)
#     response = {
#         "messages":"posts",
#         "data":serializer.data
#     }
#     return Response(data=response, status=status.HTTP_200_OK)

# @api_view(http_method_names=['PUT'])
# def update_post(request:Request,post_id:int):
#     post = get_object_or_404(Post, pk=post_id)
#     data = request.data 
#     serializer = PostSerializer(instance=post, data=data)

#     if serializer.is_valid():
#         serializer.save()
#         response = {
#             "messages":"Post Updated Successfully",
#             "data":serializer.data
#         }
#         return Response(data=response, status=status.HTTP_200_OK)
#     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(http_method_names=['DELETE'])
# def delete_post(request:Request,post_id:int):
#     post = get_object_or_404(Post, pk=post_id)
#     post.delete()

#     return Response(status=status.HTTP_204_NO_CONTENT)



















# from rest_framework.request import Request
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.decorators import api_view, APIView
# from .models import Post
# from .serializers import PostSerializer
# from django.shortcuts import get_object_or_404

# from posts import serializers

# @api_view(http_method_names=["GET", "POST"])
# def homepage(request:Request):

#     if request.method == "POST":
#         data = request.data
#         response={'message':'Hello World', 'data':data}
#         return Response(data=response, status=status.HTTP_201_CREATED)

#     response={'message':'Hello World'}
#     return Response(data=response, status=status.HTTP_200_OK)


# ## REMOVED 
# # @api_view(http_method_names=['GET', 'POST'])
# # def list_posts(request:Request):
# #     posts = Post.objects.all()
# #     if request.method == 'POST':
# #         data = request.data
# #         serializer = PostSerializer(data=data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             response={
# #                 "message":"Post Created",
# #                 "data":serializer.data
# #             }
# #             return Response(data=response, status=status.HTTP_201_CREATED)
# #         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# #     serializer = PostSerializer(instance=posts, many=True)
# #     response = {
# #         "messages":"posts",
# #         "data":serializer.data
# #     }

# #     return Response(data=response, status=status.HTTP_200_OK)

# class PostListCreateView(APIView):
#     serializer_class = PostSerializer

#     """ a view for creating and listing posts """
#     def get(self, request:Request, *args, **kwargs):
#         posts = Post.objects.all()
#         serializer = self.serializer_class(instance=posts, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK) 

#     def post(self, request:Request, *args, **kwargs):
#         data = request.data 
#         serializer = self.serializer_class(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             response = {
#                 "message":"Post Created!",
#                 "data":serializer.data
#             }
#             return Response(data=response, status=status.HTTP_201_CREATED) 

# @api_view(http_method_names=['GET'])
# def post_detail(request:Request, post_id:int):
#     post = get_object_or_404(Post, pk=post_id)
#     serializer = PostSerializer(instance=post)
#     response = {
#         "messages":"posts",
#         "data":serializer.data
#     }
#     return Response(data=response, status=status.HTTP_200_OK)

# @api_view(http_method_names=['PUT'])
# def update_post(request:Request,post_id:int):
#     post = get_object_or_404(Post, pk=post_id)
#     data = request.data 
#     serializer = PostSerializer(instance=post, data=data)

#     if serializer.is_valid():
#         serializer.save()
#         response = {
#             "messages":"Post Updated Successfully",
#             "data":serializer.data
#         }
#         return Response(data=response, status=status.HTTP_200_OK)
#     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(http_method_names=['DELETE'])
# def delete_post(request:Request,post_id:int):
#     post = get_object_or_404(Post, pk=post_id)
#     post.delete()

#     return Response(status=status.HTTP_204_NO_CONTENT)
















# from rest_framework.request import Request
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.decorators import api_view
# from .models import Post
# from .serializers import PostSerializer
# from django.shortcuts import get_object_or_404

# from posts import serializers

# @api_view(http_method_names=["GET", "POST"])
# def homepage(request:Request):

#     if request.method == "POST":
#         data = request.data
#         response={'message':'Hello World', 'data':data}
#         return Response(data=response, status=status.HTTP_201_CREATED)

#     response={'message':'Hello World'}
#     return Response(data=response, status=status.HTTP_200_OK)

# @api_view(http_method_names=['GET', 'POST'])
# def list_posts(request:Request):
#     posts = Post.objects.all()
#     if request.method == 'POST':
#         data = request.data
#         serializer = PostSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             response={
#                 "message":"Post Created",
#                 "data":serializer.data
#             }
#             return Response(data=response, status=status.HTTP_201_CREATED)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     serializer = PostSerializer(instance=posts, many=True)
#     response = {
#         "messages":"posts",
#         "data":serializer.data
#     }

#     return Response(data=response, status=status.HTTP_200_OK)

# @api_view(http_method_names=['GET'])
# def post_detail(request:Request, post_id:int):
#     post = get_object_or_404(Post, pk=post_id)
#     serializer = PostSerializer(instance=post)
#     response = {
#         "messages":"posts",
#         "data":serializer.data
#     }
#     return Response(data=response, status=status.HTTP_200_OK)

# @api_view(http_method_names=['PUT'])
# def update_post(request:Request,post_id:int):
#     post = get_object_or_404(Post, pk=post_id)
#     data = request.data 
#     serializer = PostSerializer(instance=post, data=data)

#     if serializer.is_valid():
#         serializer.save()
#         response = {
#             "messages":"Post Updated Successfully",
#             "data":serializer.data
#         }
#         return Response(data=response, status=status.HTTP_200_OK)
#     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(http_method_names=['DELETE'])
# def delete_post(request:Request,post_id:int):
#     post = get_object_or_404(Post, pk=post_id)
#     post.delete()

#     return Response(status=status.HTTP_204_NO_CONTENT)
















# from rest_framework.request import Request
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.decorators import api_view
# from .models import Post
# from .serializers import PostSerializer
# from django.shortcuts import get_object_or_404

# from posts import serializers

# @api_view(http_method_names=["GET", "POST"])
# def homepage(request:Request):

#     if request.method == "POST":
#         data = request.data
#         response={'message':'Hello World', 'data':data}
#         return Response(data=response, status=status.HTTP_201_CREATED)

#     response={'message':'Hello World'}
#     return Response(data=response, status=status.HTTP_200_OK)

# @api_view(http_method_names=['GET', 'POST'])
# def list_posts(request:Request):
#     posts = Post.objects.all()
#     if request.method == 'POST':
#         data = request.data
#         serializer = PostSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             response={
#                 "message":"Post Created",
#                 "data":serializer.data
#             }
#             return Response(data=response, status=status.HTTP_201_CREATED)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     serializer = PostSerializer(instance=posts, many=True)
#     response = {
#         "messages":"posts",
#         "data":serializer.data
#     }

#     return Response(data=response, status=status.HTTP_200_OK)

# @api_view(http_method_names=['GET'])
# def post_detail(request:Request, post_id:int):
#     post = get_object_or_404(Post, pk=post_id)
#     serializer = PostSerializer(instance=post)
#     response = {
#         "messages":"posts",
#         "data":serializer.data
#     }
#     return Response(data=response, status=status.HTTP_200_OK)

    













# from rest_framework.request import Request
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.decorators import api_view

# posts=[

#     {
#         'id':1,
#         'title':'title1',
#         'content':'content1'
#     },
#      {
#         'id':2,
#         'title':'title2',
#         'content':'content2'
#     },
#     {
#         'id':3,
#         'title':'title3',
#         'content':'content3'
#     }

# ]

# @api_view(http_method_names=["GET", "POST"])
# def homepage(request:Request):

#     if request.method == "POST":
#         data = request.data
#         response={'message':'Hello World', 'data':data}
#         return Response(data=response, status=status.HTTP_201_CREATED)

#     response={'message':'Hello World'}
#     return Response(data=response, status=status.HTTP_200_OK)

# @api_view(http_method_names=['GET'])
# def list_posts(request:Request):
#     return Response(data=posts, status=status.HTTP_200_OK)

# @api_view(http_method_names=['GET'])
# def post_detail(request:Request, post_index:int):
#     post = posts[post_index]

#     if post:
#         return Response(data=post, status=status.HTTP_200_OK)

#     return Response(data={"error":"Post not found"}, status=status.HTTP_404_NOT_FOUND)













# from rest_framework.request import Request
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.decorators import api_view

# @api_view(http_method_names=["GET", "POST"])
# def homepage(request:Request):

#     if request.method == "POST":
#         data = request.data
#         response={'message':'Hello World', 'data':data}
#         return Response(data=response, status=status.HTTP_201_CREATED)

#     response={'message':'Hello World'}
#     return Response(data=response, status=status.HTTP_200_OK)











# from django.shortcuts import render
# from django.http import HttpRequest, HttpResponse, JsonResponse
# # Create your views here.

# def homepage(request:HttpRequest):
#     response={'message':'Hello World'}
#     return JsonResponse(data=response)
