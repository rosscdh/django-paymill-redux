# -*- coding: utf-8 -*-
"""
Webhook signals
"""
from django.dispatch import Signal

#
# Outgoing Events
#
paymill_event = Signal(providing_args=['event_name'])
