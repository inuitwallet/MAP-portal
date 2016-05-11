from map.models import Profile
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = serializers.HyperlinkedRelatedField(view_name='profile',
                                                  queryset=Profile.objects.all())

    class Meta:
        model = User
        fields = (
            'username',
            'profile'
        )


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Profile
        fields = (
            'user',
            'mouse_sonar',
            'focus_border',
            'show_sounds',
            'magnifier',
            'on_screen_keyboard'
        )
