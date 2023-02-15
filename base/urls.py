from django.urls import path
from rest_framework.routers import DefaultRouter
from .import views


router = DefaultRouter()

router.register('blogs', views.BlogViewSet, basename='blogs')
router.register('categories', views.CategoryViewSet, basename='categories')

urlpatterns = router.urls
