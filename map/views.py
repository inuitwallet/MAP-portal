from django.shortcuts import render
from map.models import Profile
from django.contrib.auth.models import User
from rest_framework import generics
from map.serializers import ProfileSerializer, UserSerializer
from .permissions import IsUser, IsProfileOwner


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = (IsUser,)


class Profiles(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsProfileOwner,)


def index(request):
    return render(request, 'index.html', )
