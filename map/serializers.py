from django.contrib.auth.models import User, Group
from rest_framework import serializers


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
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
