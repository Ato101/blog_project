from django.shortcuts import render
from .models import Features

def index(request):
    features= Features.objects.all()
    return render(request,'index.html',{'features':features})
def post(request,pk):
    features = Features.objects .get(id=pk)
    return render(request,'post.html',{'features':features})