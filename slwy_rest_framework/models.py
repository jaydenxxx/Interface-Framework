from slwy_rest_framework.fields import Field, Header
import requests
import json


class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs,):
        if name == 'PostAPI':
            return type.__new__(cls, name, bases, attrs)
        mappings = dict()

        attrs['headers'] = Header()
        for k, v in attrs.items():
            if isinstance(v, Field):
                mappings[k] = v

        for k in mappings.keys():
            attrs.pop(k)

        attrs['__mappings__'] = mappings

        try:
            attrs['__url__'] = attrs.get('Meta').url
        except AttributeError:
            raise Exception("you must set api request url in class Meta!")

        return type.__new__(cls, name, bases, attrs)


class PostAPI(dict, metaclass=ModelMetaClass):
    def __init__(self, *args, **kwargs):
        super(PostAPI, self).__init__(*args, **kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def as_view(self):
        # 请求参数
        request_data = self.__mappings__['params']
        if isinstance(request_data.data, dict):
            request_data = json.dumps(request_data.data)

        # 请求headers
        request_headers = self.__mappings__['headers'].data
        if not isinstance(request_headers, dict):
            raise TypeError("headers must be a dict type!")

        response = requests.post(url=self.__url__, data=request_data, headers=request_headers)
        return response
