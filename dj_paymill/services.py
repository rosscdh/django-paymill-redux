# -*- coding: utf-8 -*-
from django.conf import settings

PRIVATE_API_KEY = settings.PAYMILL.get('PRIVATE_API_KEY', None)

assert PRIVATE_API_KEY is not None, 'You must define a PAYMILL.PRIVATE_API_KEY'

from .signals import paymill_event

import logging
logger = logging.getLogger('django.request')


class PaymillWebhookService(object):
    client = None
    stamp_data = None
    stamp_serial = None

    def __init__(self, *args, **kwargs):
        # Allow overrides
        self.key = kwargs.get('key', PRIVATE_API_KEY)
        # self.client = Client(self.key, self.secret)

    def process(self, data):
        """
        Method to process the callback data
        """
        # data = self.client.call({'data': data.get('data')})

        if data is not None:

            logger.info('Provided data: %s' % data)
            # pop the stamp_serial from the data so its not repeated
            # self.stamp_serial = data.pop('serial', None)
            # logger.info('Provided with stamp serial: %s' % self.stamp_serial)

            # issue the signal
            paymill_event.send(sender=self, event_name=event_name, **data)

        return data
