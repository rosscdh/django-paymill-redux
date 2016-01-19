django-paymill
====================

A Django app for integrating with paymill


Installation
------------

1. python setup.py
2. pip install requirements.txt
3. add dj_paymill to INSTALLED_APPS
4. add url to paymill endpoint
5. register url with paymill as webhook callback

Settings
--------


__Required__


```
PAYMILL = {
    'PRIVATE_API_KEY': '<Your_Paymill_Private_key>',
    'WEBHOOK_URI': 'http://yourdomain.com/',  # just the domain with http(s) we manage the full path
}
```


__Example Implementation__

1. Setup your urls.py to use the view below as the callback reciever or just use the default sss reciever
2. Register the url "https://yourhost.com/sss/webhook/" as the webhook callback at paymill
3. and that is it, you can now hook up the signal listener and get a signal event whenever a webhook event happens

```
url(r'^paymill/', include('dj_paymill.urls', namespace='paymill')),
```

__Or__

You can write a custom view, by extending our View and doing somethign more specific with the data, and hook the view up to a url and register that url with paymill.

```views.py
from dj_paymill.views import PaymillView


class MyPaymillViewWebhookRecieverView(PaymillView):
    def post(self, request, *args, **kwargs):
        # do something amazing

        return self.render_json_response({
            'detail': 'Paymill Callback recieved',
            'data': kwargs
        })
```


__Please Note__

If you use the PaymillView then a signal will be issued when recieving callbacks from paymill, which you can then listen for and do other amazing things.


__Signal Example Implementation__


```signals.py
from django.dispatch import receiver

from paymill.signals import paymill_event


@receiver(paymill_event)
def on_paymill_callback(sender, **kwargs):
    # do something amazing with the data in the kwargs dict
    pass
```


__TODO__

1. ~~tests~~
2. ~~more descriptive readme.md~~
3. improve setup.py to install from requirements
4. ~~fix broken python_sdk install cant install from pip lacks setup.py~~
