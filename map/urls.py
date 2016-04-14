from django.conf.urls import url
from userena.urls import merged_dict
from userena import settings as userena_settings
from userena import views as userena_views
from django.contrib.auth import views as auth_views
from userena.compat import auth_views_compat_quirks, password_reset_uid_kwarg
from map import views as map_views

urlpatterns = [
    # Signup, signin and signout
    url(r'^signup/$',
        userena_views.signup,
        {'template_name': 'map/signup_form.html'},
        name='userena_signup'),
    url(
        r'^signin/',
        userena_views.signin,
        {'template_name': 'map/signin_form.html'},
        name="userena_signin"
    ),
    url(r'^signout/$',
        userena_views.signout,
        {'template_name': 'map/signout.html'},
        name='userena_signout'),

    # Reset password
    url(
        r'^password/reset/$',
        auth_views.password_reset,
        merged_dict(
            {
                'template_name': 'map/password_reset_form.html',
                'email_template_name': 'map/emails/password_reset_message.txt',
                'extra_context': {
                    'without_usernames': userena_settings.USERENA_WITHOUT_USERNAMES
                }
            },
            auth_views_compat_quirks['userena_password_reset']
        ),
        name='userena_password_reset'
    ),
    url(
        r'^password/reset/done/$',
        auth_views.password_reset_done,
        {'template_name': 'map/password_reset_done.html'},
        name='userena_password_reset_done'
    ),
    url(
        r'^password/reset/confirm/(?P<%s>[0-9A-Za-z]+)-(?P<token>.+)/$' %
        password_reset_uid_kwarg,
        auth_views.password_reset_confirm,
        merged_dict(
            {
                'template_name': 'map/password_reset_confirm_form.html',
            },
            auth_views_compat_quirks['userena_password_reset_confirm']
        ),
        name='userena_password_reset_confirm'
    ),
    url(
        r'^password/reset/confirm/complete/$',
        auth_views.password_reset_complete,
        {
            'template_name': 'map/password_reset_complete.html'
        },
        name='userena_password_reset_complete'),

    # Signup
    url(
        r'^(?P<username>[\@\.\w-]+)/signup/complete/$',
        userena_views.direct_to_user_template,
        {
            'template_name': 'map/signup_complete.html',
            'extra_context': {
                'userena_activation_required':
                    userena_settings.USERENA_ACTIVATION_REQUIRED,
                'userena_activation_days': userena_settings.USERENA_ACTIVATION_DAYS
            }
        },
        name='userena_signup_complete'),

    # Activate
    url(
        r'^activate/(?P<activation_key>\w+)/$',
        userena_views.activate,
        {
            'template_name': 'map/activate_fail.html',
            'retry_template_name': 'map/activate_retry.html',
            'success_url': 'index'
        },
        name='userena_activate'
    ),

    # Retry activation
    url(
        r'^activate/retry/(?P<activation_key>\w+)/$',
        userena_views.activate_retry,
        {
            'template': 'map/activate_retry_success.html'
        },
        name='userena_activate_retry'
    ),

    # Change email and confirm it
    url(
        r'^(?P<username>[\@\.\w-]+)/email/$',
        userena_views.email_change,
        {
            'template_name': 'map/email_form.html'
        },
        name='userena_email_change'
    ),
    url(
        r'^(?P<username>[\@\.\w-]+)/email/complete/$',
        userena_views.direct_to_user_template,
        {
            'template_name': 'map/email_change_complete.html'
        },
        name='userena_email_change_complete'
    ),
    url(
        r'^(?P<username>[\@\.\w-]+)/confirm-email/complete/$',
        userena_views.direct_to_user_template,
        {
            'template_name': 'map/email_confirm_complete.html'
        },
        name='userena_email_confirm_complete'
    ),
    url(
        r'^confirm-email/(?P<confirmation_key>\w+)/$',
        userena_views.email_confirm,
        {
            'template_name': 'map/email_confirm_fail.html'
        },
        name='userena_email_confirm'
    ),

    # Disabled account
    url(
        r'^(?P<username>[\@\.\w-]+)/disabled/$',
        userena_views.disabled_account,
        {
            'template_name': 'map/disabled.html'
        },
        name='userena_disabled'
    ),

    # Change password
    url(
        r'^(?P<username>[\@\.\w-]+)/password/$',
        userena_views.password_change,
        {
            'template_name': 'map/password_form.html'
        },
        name='userena_password_change'
    ),
    url(
        r'^(?P<username>[\@\.\w-]+)/password/complete/$',
        userena_views.direct_to_user_template,
        {
            'template_name': 'map/password_complete.html'
        },
        name='userena_password_change_complete'
    ),

    # Edit profile
    #url(
    #    r'^(?P<username>[\@\.\w-]+)/edit/$',
    #    userena_views.profile_edit,
    #    {
    #        'template_name': 'map/profile_form.html'
    #    },
    #    name='userena_profile_edit'
    #),

    # View profiles
    url(
        r'^(?P<username>(?!(signout|signup|signin)/)[\@\.\w-]+)/$',
        userena_views.profile_edit,
        {
            'template_name': 'map/profile_form.html'
        },
        name='userena_profile_edit'
    ),
    url(
        r'^page/(?P<page>[0-9]+)/$',
        userena_views.ProfileListView.as_view(),
        {
            'template_name': 'map/profile_list.html'
        },
        name='userena_profile_list_paginated'
    ),
    url(
        r'^$',
        map_views.index,
        name='index'
    ),
]
