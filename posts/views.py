# django imports
from django.shortcuts import render, redirect
from django.http import HttpResponse, request

# Models e serializer
from .models import Posts
from .serializer import PostsSerializer

# rest framework imports
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
def index(request):
    #return HttpResponse('Hello')
    posts = Posts.objects.all()[:10]

    context = {
        'title': 'Yago',
        'posts': posts
    }
    return render(request, 'posts/index.html', context)
'''
    return render(request, 'posts/index.html',{
       'title' : 'Posts'
    })
'''
def details (request, id):
    post = Posts.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request, 'posts/details.html', context)

def add (request):
    
    if(request.method == 'POST'):
        
        title = request.POST['title']
        body = request.POST['body']

        post = Posts(title=title, body=body)
        post.save()

        return redirect('/posts')
    else:
        return render(request, 'posts/add.html')

"""
    Criando classes ue auxiliam api rest
"""
class PostsListView(APIView):
    serializer_class = PostsSerializer # pegando uma instancia do objeto serializado

    def get(self, request, format=None):
        serializer = self.serializer_class(Posts.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(): # se ampos serializados sao válidos salva os dados
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: # senao, retornne um erro!!
            return Response({"message": "403 Forbidden"}, status=status.HTTP_409_CONFLICT)
    
class PostsView(APIView):
    def get(self, request, pk, format=None):
        posts = Posts.objects.get(pk=pk)
        serializer = PostsSerializer(posts)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = Posts.objects.get(pk=pk)
        serializer = PostsSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = Posts.objects.get(pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    