from slwy_rest_framework.fields import Field, Header
import requests
import json


class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs,):
        if name == 'PostAPI':
            return type.__new__(cls, name, bases, attrs)
        mappings = dict()

        Headers = Header()
        Headers.data['Authorization'] = LoginAPI().get_auth()
        attrs['headers'] = Headers
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


class LoginAPI:
    headers = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json;charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 Safari/601.1 wechatdevtools/1.02.1808101 MicroMessenger/6.5.7 Language/zh_CN webview/15355365235235902 webdebugger port/62427",
        }
    loginName = "13982228044"
    userPassword = "E10ADC3949BA59ABBE56E057F20F883E"
    partnerCode = 1
    partnerType = "04"
    __data_dict = {
        "loginName": loginName,
        "userPassword": userPassword,
        "partnerCode": partnerCode,
        "partnerType": partnerType
    }
    data = json.dumps(__data_dict)
    login_url = "http://172.17.1.249:34007/cuser/cuserinfo/login"
    response = None

    def get(self):
        response = requests.post(url=self.login_url, data=self.data, headers=self.headers)
        self.response = response
        return response

    def get_auth(self):
        self.get()
        response = self.response

        if response.status_code != 200:
            raise Exception("login api request fails!")

        response_dict = json.loads(response.text)

        if response_dict['code'] != 1:
            raise Exception(response_dict['message'])

        return response_dict['data']['token']


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
