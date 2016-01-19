# -*- coding: utf-8 -*-
from django.conf import settings


ACCEPTED_EVENTS = getattr(settings.PAYMILL, 'ACCEPTED_EVENTS', (
        'chargeback.executed',
        'client.updated',
        'fraud.created',
        'invoice.available',
        'payment.expired',
        'payout.transferred',
        'refund.created',
        'refund.failed',
        'refund.succeeded',
        'subscription.activated',
        'subscription.deactivated',
        'subscription.canceled',
        'subscription.created',
        'subscription.deleted',
        'subscription.expiring',
        'subscription.failed',
        'subscription.succeeded',
        'subscription.updated',
        'transaction.created',
        'transaction.failed',
        'transaction.succeeded',
        'transaction.updated',
        'transaction.pending',
        'app.merchant.activated',
        'app.merchant.deactivated',
        'app.merchant.app.disabled',
        'app.merchant.live_requests_allowed',
        'app.merchant.live_requests_not_allowed',
        'app.merchant.rejected',
        'app.merchant.pm.updated',
))