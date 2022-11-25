import requests

from generalutils.PropertiesUtils import PropertiesUtils


class ApiUtils:

    __url = PropertiesUtils.read_config_data("yt_url")

    @classmethod
    def post(cls, endpoint, headers, params):
        return requests.request("GET", cls.__url + endpoint, headers=headers, params=params)
