__author__ = 'jmeireles'
import os
import requests
from urllib import urlencode
from urlparse import parse_qs, urlsplit, urlunsplit


class Helper:

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

    @staticmethod
    def set_query_parameter(url, param_name, param_value):
        """Given a URL, set or replace a query parameter and return the
        modified URL.

        >>> set_query_parameter('http://example.com?foo=bar&biz=baz', 'foo', 'stuff')
        'http://example.com?foo=stuff&biz=baz'

        """
        scheme, netloc, path, query_string, fragment = urlsplit(url)
        query_params = parse_qs(query_string)

        query_params[param_name] = [param_value]
        new_query_string = urlencode(query_params, doseq=True)

        return urlunsplit((scheme, netloc, path, new_query_string, fragment))