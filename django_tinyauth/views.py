# -*- coding: utf-8 -*-

import urlparse
from django.conf import settings
from django.contrib.auth import login as auth, get_backends
from django.contrib.auth.views import login
from django.contrib.admin.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.admin.sites import site

redirect_field_name = 'next'


def adminlogin(request):
    if request.user.is_authenticated():
        return site.index(request)

    users = User.objects.all()
    return login(request,
                 template_name='tinylogin.html',
                 extra_context={'users': users})


def tinylogin(request, pk):
    user = User.objects.get(pk=pk)
    redirect_to = request.REQUEST.get(redirect_field_name, '')
    netloc = urlparse.urlparse(redirect_to)[1]

    # Use default setting if redirect_to is empty
    if not redirect_to:
        redirect_to = settings.LOGIN_REDIRECT_URL

        # Heavier security check -- don't allow redirection to a different
        # host.
    elif netloc and netloc != request.get_host():
        redirect_to = settings.LOGIN_REDIRECT_URL

    if user:
        backend = get_backends()[0]
        user.backend = "%s.%s" % (backend.__module__,
                                  backend.__class__.__name__)
        auth(request, user)
        return HttpResponseRedirect(redirect_to)
    else:
        redirect('/admin/')
