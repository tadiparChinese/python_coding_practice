##urls
from django.contrib import admin
from django.urls import path, include
from api import view
from rest_framework.routers import DefaultRouter

#creating router object
router = DefaultRouter()

#register StudentViewSet with Router

router.register('studentapi', views.StudentModelViewSet, basename='student')

#also
router.register('studentapi', views.StudentReadOnlyModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
] 


#views

from .models import Student
from .serializer import StudentSerializer
from rest_framework import viewsets

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



#also
class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet): #incase of readonly api to user eg: CovidAPI
    queryset = Student.objects.all()
    serializer_class = StudentSerializer