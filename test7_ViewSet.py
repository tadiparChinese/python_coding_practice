#in viewSets you dont need to maintain the url, just create router, register your class with router so that bar bar urls likhne ke jaroorat nahi


#router defining

from django.contrib import admin
from django.urls import path, include
from api import view
from rest_framework.routers import DefaultRouter

#creating router object
router = DefaultRouter()

#register StudentViewSet with Router

router.register('studentapi', views.StudentViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]


#views

from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
from rest_framework import status 
from rest_framework import viewsets


class StudentViewSet(viewsets.Viewset):
    def list(self, request):
        print("********List*********")
        print("Basename: ". self.basename)
        print("Action: ". self.action)
        print("Detail: ". self.detail)
        print("Suffix: ". self.suffix)
        print("Name: ". self.name)
        print("Description: ". self.description)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        print("********Retrieve*********")
        print("Basename: ". self.basename)
        print("Action: ". self.action)
        print("Detail: ". self.detail)
        print("Suffix: ". self.suffix)
        print("Name: ". self.name)
        print("Description: ". self.description)
        id = pk
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def create(self, request, pk=None, format=None):
        print("********Create*********")
        print("Basename: ". self.basename)
        print("Action: ". self.action)
        print("Detail: ". self.detail)
        print("Suffix: ". self.suffix)
        print("Name: ". self.name)
        print("Description: ". self.description)
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid( ):
            serializer.save()
            return Response({'msg':'Data created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk, format=None):
        print("********Update*********")
        print("Basename: ". self.basename)
        print("Action: ". self.action)
        print("Detail: ". self.detail)
        print("Suffix: ". self.suffix)
        print("Name: ". self.name)
        print("Description: ". self.description)
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Completely Data updated'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk):
        print("********Partial_Update*********")
        print("Basename: ". self.basename)
        print("Action: ". self.action)
        print("Detail: ". self.detail)
        print("Suffix: ". self.suffix)
        print("Name: ". self.name)
        print("Description: ". self.description)
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partialy Data updated'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        print("********Delete*********")
        print("Basename: ". self.basename)
        print("Action: ". self.action)
        print("Detail: ". self.detail)
        print("Suffix: ". self.suffix)
        print("Name: ". self.name)
        print("Description: ". self.description)
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data deleted successfully'})



