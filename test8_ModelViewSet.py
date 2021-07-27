##urls
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
    path('studentapi/', views.StudentAPI.as_view()),
    path('', include(router.urls)),
]