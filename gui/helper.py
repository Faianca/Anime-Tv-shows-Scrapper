__author__ = 'jmeireles'
import os
import requests


class Helper():

    codes = [
        200,
        301,
        302
    ]

    @staticmethod
    def get_resource_path(rel_path):
        dir_of_py_file = os.path.dirname(__file__)
        rel_path_to_resource = os.path.join(dir_of_py_file, rel_path)
        return os.path.abspath(rel_path_to_resource)

    @staticmethod
    def exists(url):
        r = requests.head(url)

        return r.status_code in Helper.codes