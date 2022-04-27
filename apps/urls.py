from django.urls import path,include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', AppViewset)


urlpatterns = [
    path('',mainView,name='main'),
    path('get-sub-categories/<int:id>',getSubCategories),
    path('detail/<int:id>',detailView,name='detail'),
    path('upload',imageUploadView),
    path('app',include(router.urls)),
    path('get-list-of-apps-data',getListOfAppData),
]