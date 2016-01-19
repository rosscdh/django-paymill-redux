# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.urlresolvers import reverse
from django.core.management.base import BaseCommand, CommandError

import urlparse
from dj_paymill import ACCEPTED_EVENTS

import paymill

assert settings.PAYMILL.get('PRIVATE_API_KEY') is not None, 'Must define PAYMILL.PRIVATE_API_KEY'
assert settings.PAYMILL.get('WEBHOOK_URI') is not None, 'Must define PAYMILL.WEBHOOK_URI'

paymill_context = paymill.PaymillContext(settings.PAYMILL.get('PRIVATE_API_KEY'))


class Command(BaseCommand):
    help = 'Registers your paymill webhook with paymill.com'

    def add_arguments(self, parser):
        parser.add_argument('--active',
                            action='store_true',
                            dest='active',
                            default=False,
                            help='Create the webhook as Active(True) or In-active(False)')

    def handle(self, *args, **options):
        local_path = reverse('paymill:paymill_webhook_callback')
        url = urlparse.urljoin(settings.PAYMILL.get('WEBHOOK_URI'), local_path)
        print url
        print options.get('active')
        print ACCEPTED_EVENTS
        resp = paymill_context.webhook_service.create_url(url, ACCEPTED_EVENTS, options.get('active'))
        print resp
