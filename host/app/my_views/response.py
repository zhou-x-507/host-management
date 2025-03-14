from rest_framework.response import Response


class DeatilResponse(Response):
    """重写响应方法"""

    def __init__(
        self,
        data=None,
        msg="success",
        status=200,
        template_name=None,
        headers=None,
        exception=False,
        code=0,
        content_type=None,
    ):
        json_data = {
            "code": code,
            "data": data,
            "msg": msg,
        }
        super().__init__(
            json_data, status, template_name, headers, exception, content_type
        )
