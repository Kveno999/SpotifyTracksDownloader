from generalutils.ApiUtils import ApiUtils
from ytapi.data import Parameters

from generalutils.FileManagerUtils import FileManagerUtils


class YoutubeApiMethods:
    headers = {
        "X-RapidAPI-Key": "",
        "X-RapidAPI-Host": ""
    }

    @classmethod
    def get_music_id(cls, search_word):
        querystring = {"query": search_word}
        response = ApiUtils.post(endpoint=Parameters.SEARCH_ENDPOINT, headers=cls.headers, params=querystring)
        return response.json()["result"]["videos"][0]["id"]

    @classmethod
    def download_music(cls, search_word):
        querystring = {"id": f"{cls.get_music_id(search_word)}", "ext": "mp4"}
        response = ApiUtils.post(endpoint=Parameters.DOWNLOAD_ENDPOINT, headers=cls.headers, params=querystring)
        url = response.json()["result"]["download_url"]
        FileManagerUtils.download_file(url, search_word)
