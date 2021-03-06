# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test.utils import override_settings

from paymill.services import PaymillWebhookService


class PaymillServiceTest(TestCase):
    """
    Test the service inits and errors correctly
    """
    subject = PaymillWebhookService

    def test_custom_key_and_secret(self):
        s = self.subject(key='new_key', secret='new_secret')
        self.assertEqual(s.key, 'new_key')
        self.assertEqual(s.secret, 'new_secret')

        self.assertEqual(s.stamp_data, None)
        self.assertEqual(s.stamp_serial, None)
