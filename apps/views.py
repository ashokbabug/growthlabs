from django.shortcuts import render,redirect
from django.http import JsonResponse
from .forms import *
from .models import *
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework import viewsets
from .permissions import CustomAdminPermission,ReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
@login_required(login_url='login')
def mainView(request):
    if request.method=='GET':
        form = AppForm()
    else:
        form = AppForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'App Created successfully')
            return redirect('main')
    apps = App.objects.all()
    context = {
        "form":form,
        "apps":apps
    }
    return render(request,'apps/user.html',context)



@api_view(['GET'])
def getSubCategories(request,id):
    s = SubCategory.objects.filter(category=id)
    serializer = AppsSerializer(s,many=True)
    return Response(serializer.data)

def detailView(request,id):
    app = App.objects.get(id=id)
    return render(request,'apps/detail.html',{'app':app})

def imageUploadView(request):
    if request.method=="POST":
        my_file = request.FILES.get('file')
        print( request.FILES)
        appid = request.POST.get('appid')
        app = App.objects.get(id=appid)
        ScreenShot.objects.create(screenshot=my_file,app=app,user=request.user)
        messages.success(request, f'uploaded successfully')
        return redirect('/')

class AppViewset(viewsets.ModelViewSet):
    '''
    in this viewset only admin can create the data.Normal User can not create the data.He can only view the data.
    This singly view can act dynamically between admin and normal use.
    It supports both basic and token authentication
    
    '''
    authentication_classes = [TokenAuthentication,BasicAuthentication]
    permission_classes=[CustomAdminPermission|ReadOnly]
    queryset = App.objects.all()
    serializer_class = AppsSerializer



@api_view(['POST'])
def getListOfAppData(request):
    li = request.data['values']
    apps = App.objects.filter(id__in=li)
    serializer = AppsSerializer(apps,many=True)
    return Response(serializer.data)