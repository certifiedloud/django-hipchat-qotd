import kronos
import requests
import random
from django_hipchat_qotd.models import QOTD
from django.conf import settings


@kronos.register('0 12 * * *')
def send_to_hipchat():
    max_id = QOTD.objects.order_by('-id')[0].id
    random_id = random.randint(1, max_id + 1)
    quote = QOTD.objects.filter(id__gte=random_id)[0]

    requests.post(
        'https://api.hipchat.com/v1/rooms/message?auth_token=' + settings.HIPCHAT_AUTH_TOKEN,
        {
            'room_id': settings.HIPCHAT_ROOM_ID,
            'from': 'VW QOTD',
            'message': "{} -{}".format(quote.quote, quote.said_by),
            'color': "yellow",
            'notify': 1
        })
