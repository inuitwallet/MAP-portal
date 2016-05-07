from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
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
    # client_area_animation = models.BooleanField(default=False)
    # disable_overlapped_content = models.BooleanField(default=False)
    # mouse_click_lock = models.BooleanField(default=False)
    mouse_sonar = models.BooleanField(default=False)
    # mouse_vanish = models.BooleanField(default=False)
    # screen_reader = models.BooleanField(default=False)
    show_sounds = models.BooleanField(default=False)
    focus_border = models.IntegerField(default=1)
    magnifier = models.BooleanField(default=False)
    on_screen_keyboard = models.BooleanField(default=False)

