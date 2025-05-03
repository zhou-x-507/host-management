import logging
import subprocess

from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet

from app.my_views.serializers import HostSerializer
from app.my_views.response import DeatilResponse
from app.models import Host

logger = logging.getLogger(__name__)

class HostViewSet(GenericViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer

    def get_queryset(self):
        return super().get_queryset()

    # 查
    @action(detail=False, methods=["GET"])
    def host_list(self, request):
        serializer_data = HostSerializer(self.get_queryset(), many=True).data
        return DeatilResponse(data=serializer_data)
    
    # 增
    @action(detail=False, methods=["POST"])
    def add_host(self, request):
        ip_address = request.data.get("ipAddress")
        status = request.data.get("status")
        datacenter_id = request.data.get("datacenterId")
        Host.objects.create(ip_address=ip_address, status=status, datacenter_id=datacenter_id)
        return DeatilResponse()

    # 改
    @action(detail=False, methods=["POST"])
    def update_host(self, request):
        _id = request.data.get("id")
        ip_address = request.data.get("ipAddress")
        status = request.data.get("status")
        datacenter_id = request.data.get("datacenterId")
        Host.objects.filter(id=_id, datacenter_id=datacenter_id).update(ip_address=ip_address, status=status)
        return DeatilResponse()

    # 删
    @action(detail=False, methods=["POST"])
    def del_host(self, request):
        _id = request.data.get("id")
        Host.objects.filter(id=_id).delete()
        logger.error(f"del_host, id:{_id}, user:zx")
        return DeatilResponse()

    # ping
    @action(detail=False, methods=["GET"])
    def ping_host(self, request):
        ip_address = request.query_params.get("ipAddress")
        try:
            # 使用ping命令，-c 1表示发送一个数据包
            response = subprocess.run(['ping', '-c', '1', ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if response.returncode == 0:
                return DeatilResponse(msg=f"{ip_address} is reachable")
            else:
                return DeatilResponse(msg=f"{ip_address} is not reachable")
        except Exception as e:
            logger.error(f"ping_host, failed error:{e}")
            return DeatilResponse(msg=f"error:{e}")


# 新电脑测试