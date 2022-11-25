import requests


class FileManagerUtils:

    @staticmethod
    def download_file(url, file_name):
        download_response = requests.get(url)
        open(f"../musics/{file_name}.mp3", "wb").write(download_response.content)
