from django.http import HttpResponse
from django.shortcuts import render
from models import Profile
from rest_framework import viewsets
from serializers import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

def index(request):
    return render(request, 'index.html', )
