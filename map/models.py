from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaLanguageBaseProfile
from django.db import models


class Profile(UserenaLanguageBaseProfile):
    """
    Main class top store user details and accessibility settings
    """
    user = models.OneToOneField(
        User,
        unique=True,
        verbose_name=_('user'),
        related_name='profile'
    )
    client_area_animation = models.BooleanField(default=False)
    disable_overlapped_content = models.BooleanField(default=False)
    mouse_click_lock = models.BooleanField(default=False)
    mouse_sonar = models.BooleanField(default=False)
    mouse_vanish = models.BooleanField(default=False)
    screen_reader = models.BooleanField(default=False)
    show_sounds = models.BooleanField(default=False)
    focus_border_height = models.BigIntegerField(default=0)
    focus_border_width = models.BigIntegerField(default=0)
    message_duration = models.BigIntegerField(default=0)
    mouse_click_lock_time = models.BigIntegerField(default=0)
    high_contrast = models.CharField(max_length=200)
    audio_description = models.CharField(max_length=200)

