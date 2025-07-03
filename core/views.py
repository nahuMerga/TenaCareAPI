from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Remedies, HealthTips, FirstAid
from .serializers import RemediesSerializer, HealthTipsSerializer, FirstAidSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny


# Create your views here.
class RemediesListView(ListAPIView):
    queryset = Remedies.objects.all()
    serializer_class = RemediesSerializer
    permission_classes = [AllowAny]

class RemediesDetailView(RetrieveAPIView):
    queryset = Remedies.objects.all()
    serializer_class = RemediesSerializer
    permission_classes = [AllowAny]
    lookup_field = 'id'

class HealthTipsListView(ListAPIView):
    queryset = HealthTips.objects.all()
    serializer_class = HealthTipsSerializer
    permission_classes = [AllowAny]
    
class FirstAidListView(ListAPIView):
    queryset = FirstAid.objects.all()
    serializer_class = FirstAidSerializer
    permission_classes = [AllowAny]
