from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *

def home(request):
    user_list = UserName.objects.order_by('name')
    posts = Post.objects.all
    context = {'user_list': user_list , 'posts' : posts }
    return render(request, 'app/home.html', context)

    
class userView(APIView):
    
    serializer_name = UserNameSerializer
    serializer_class = PostSerializer
    def get(self, username):
        detail = [ {"author": detail.author,"title": detail.title,"file":detail.file , "visible":detail.visible} 
        for detail in Post.objects.filter(visible__icontains=username)]
        return Response(detail)
  
    def post(self, request):
  
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return  Response(serializer.data)