from django.shortcuts import render,redirect
from django.http import JsonResponse
from .forms import *
from .models import *
from rest_framework.decorators import api_view,permission_classes
from .serializers import *
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework import viewsets
from .permissions import CustomAdminPermission,ReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
@login_required(login_url='login')
def mainView(request):
    '''It is a main page it will render an app creation and image upload form dynamically based on the user type
    If the user is an admin user then it will load a form for app creation else it will load a list of all apps 
    with is conneted to a detail view on click'''
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

@login_required(login_url='login')
def detailView(request,id):
    '''It returns an html page with detailed description of the app and drag and drop feature for image upload'''
    app = App.objects.get(id=id)
    return render(request,'apps/detail.html',{'app':app})

@login_required(login_url='login')
def imageUploadView(request):
    '''This view act as an end point for screenshot upload.it will return a success message on successfull upload of the screenshot'''
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
@permission_classes([IsAuthenticated])
def getListOfAppData(request):
    '''This view returns all the list of app data submitted
    Eg:By passing the values like [1,2,3] it return the onlly 1,2,3 apps in json format'''
    li = request.data['values']
    apps = App.objects.filter(id__in=li)
    serializer = AppsSerializer(apps,many=True)
    return Response(serializer.data)