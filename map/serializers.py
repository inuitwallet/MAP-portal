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
            'client_area_animation',
            'disable_overlapped_content',
            'mouse_click_lock',
            'mouse_sonar',
            'mouse_vanish',
            'screen_reader',
            'show_sounds',
            'focus_border_height',
            'focus_border_width',
            'message_duration',
            'mouse_click_lock_time',
            'high_contrast',
            'audio_description'
        )
