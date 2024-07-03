from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from blog.api.post import PostViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
