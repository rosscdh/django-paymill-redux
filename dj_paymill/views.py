# -*- coding: utf-8 -*-
from django.views.generic import View

from django.http import JsonResponse

from . import ACCEPTED_EVENTS
from .services import PaymillWebhookService

import logging
logger = logging.getLogger('django.request')


class PaymillView(JsonResponse, View):
    """
    Handle the paymill callback
    """
    accepted_events = ACCEPTED_EVENTS

    json_dumps_kwargs = {'indent': 3}

    service = None
    # stamp_serial = None
    # stamp_data = None

    def dispatch(self, request, *args, **kwargs):
        logger.info('Recieved paymill webhook')
        self.service = PaymillWebhookService()

        if request.method.lower() in self.accepted_events:
            self.stamp_serial, self.stamp_data = self.service.process(data=request.POST)

        return super(PaymillView, self).dispatch(request=request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.render_json_response({
            'detail': 'Paymill Callback recieved',
            'data': self.stamp_data,
        })
