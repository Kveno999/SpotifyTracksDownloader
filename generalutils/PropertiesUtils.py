import json


class PropertiesUtils:

    @staticmethod
    def get_relative_path_from_config(file):
        rel_path = f"../configuration/{file}"
        return rel_path

    @classmethod
    def read_config_data(cls, item):
        f = open(cls.get_relative_path_from_config("config.json"), 'r')
        data_config = json.load(f)
        return data_config[item]
