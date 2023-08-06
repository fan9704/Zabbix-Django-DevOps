import json
import logging
from channels import Group
from django.core.management import BaseCommand
from django.conf import settings
import redis

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Subscribe the zabbix alerts channels'
    def handle(self, *args, **options):
        rc = redis.Redis(
            host=settings.REDIS_OPTIONS['HOST'],
            password=settings.REDIS_OPTIONS['PASSWD'],
            port=settings.REDIS_OPTIONS['PORT'],
            db=settings.REDIS_OPTIONS['DB'],
        )
        rc.delete(settings.GROUP_NAME)
        pubsub = rc.pubsub()
        pubsub.subscribe(settings.GROUP_NAME)
        for item in pubsub.listen():
            if item["type"] == 'message':
                Group(settings.GROUP_NAME).send({
                    'text':bytes.decode("data")
                })
                logger.debug("send a message    %s"%item)
