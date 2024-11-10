from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlatformViewSet, PatchViewSet, TestViewSet, BugViewSet

router = DefaultRouter()
router.register(r'platforms', PlatformViewSet)
router.register(r'patches', PatchViewSet)
router.register(r'tests', TestViewSet)
router.register(r'bugs', BugViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
