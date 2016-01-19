# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.decorators.csrf import csrf_exempt

from .views import PaymillView


urlpatterns = patterns('',
                       url(r'^webhook/$',
                           csrf_exempt(PaymillView.as_view()),
                           name='paymill_webhook_callback'),
)
