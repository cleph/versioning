from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Platform, Patch, Test, Bug
from .serializers import PlatformSerializer, PatchSerializer, TestSerializer, BugSerializer

class PlatformViewSet(viewsets.ModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer

class PatchViewSet(viewsets.ModelViewSet):
    queryset = Patch.objects.all()
    serializer_class = PatchSerializer

    def create(self, request, *args, **kwargs):
        platform = Platform.objects.get(id=request.data['platform'])
        if platform.status not in ['PreAlpha', 'Alpha', 'Beta', 'Gamma', 'RC', 'Rolling']:
            return Response({'error': 'Patch not allowed for this platform status.'}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    def create(self, request, *args, **kwargs):
        platform = Platform.objects.get(id=request.data['platform'])
        if platform.status not in ['PreAlpha', 'Alpha', 'Beta', 'Gamma', 'RC']:
            return Response({'error': 'Test not allowed for this platform status.'}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

class BugViewSet(viewsets.ModelViewSet):
    queryset = Bug.objects.all()
    serializer_class = BugSerializer

    def create(self, request, *args, **kwargs):
        platform = Platform.objects.get(id=request.data['platform'])
        if platform.status not in ['PreAlpha', 'Alpha', 'Beta']:
            return Response({'error': 'Bug not allowed for this platform status.'}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)
