import logging
from datetime import datetime

from celery import shared_task
from django.db.models import Count, F
from app.models import Datacenter, Host, HostCount

logger = logging.getLogger(__name__)


@shared_task
def collect_host_stats():
    datetime_now = datetime.now()
    logger.info(f":::::collect_host_stats start:::::{datetime_now}")

    host_counts = Datacenter.objects.annotate(
        datacenter_id=F('id'),
        count=Count('host')
    ).values('city_id', 'datacenter_id', 'count')

    _list = []
    for item in host_counts:
        item["create_datetime"] = datetime_now
        _list.append(HostCount(**item))

    HostCount.objects.bulk_create(_list)
    logger.info(f":::::collect_host_stats end:::::{len(_list)}")
