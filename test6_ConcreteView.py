#Note: ListAPIView = GenericAPIView + Mixins : inhereting properties from genericapiview and mixins

from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIVIew, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView,



#note: only use  ListCreateAPIView and RetrieveUpdateDestroyAPIView rest will be included in these two
#dont write all these classes 
class StudentList(ListAPIView): #get
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentCreate(CreateAPIView): #post
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieve(RetrieveAPIView): #Retrieve
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentUpdate(UpdateAPIVIew): #Update
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDestroy(DestroyAPIView): #Destroy
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentListCreate(ListCreateAPIView): #ListCreate (this one needed)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdate(RetrieveUpdateAPIView): #RetrieveUpdate
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveDestroy(RetrieveDestroyAPIView): #RetrieveDestroy
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView): #RetrieveUpdateDestroy (and this one also needed, rest dont use it)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


#note: only use  ListCreateAPIView and RetrieveUpdateDestroyAPIView rest will be included in these two

class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

##urls
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('studentapi/', views.StudentList.as_view()),
    path('studentapi/', views.StudentCreate.as_view()),
    path('studentapi/<int:pk>', views.StudentRetrieve.as_view()),
    path('studentapi/<int:pk>', views.StudentUpdate.as_view()),
    path('studentapi/<int:pk>/', views.StudentDestroy.as_view()),
    path('studentapi/', views.StudentListCreate.as_view()),
    path('studentapi/<int:pk>/', views.StudentRetrieveUpdate.as_view()),
    path('studentapi/<int:pk>/', views.StudentRetrieveDestroy.as_view()),
    path('studentapi/<int:pk>/', views.StudentRetrieveUpdateDestroy.as_view()),
]