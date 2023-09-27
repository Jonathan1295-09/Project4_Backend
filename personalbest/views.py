from .models import personalBest
from rest_framework import viewsets, permissions
from .serializers import PersonalBestSerializer

class PersonalBestViewSet(viewsets.ModelViewSet):
    queryset = personalBest.objects.all()
    serializer_class = PersonalBestSerializer
    permission_classes = [permissions.AllowAny,]