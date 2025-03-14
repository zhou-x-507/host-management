import os
from celery import Celery

# 设置Django的默认配置模块
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'host.settings')

app = Celery('host')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(['app.tasks'])
