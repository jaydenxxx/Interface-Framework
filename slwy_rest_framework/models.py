from slwy_rest_framework.fields import Field, Header
import requests
import json


class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
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

        # try:
        #     attrs['__url__'] = attrs.get('Meta').url
        # except AttributeError:
        #     raise Exception("you must set api request url in class Meta!")

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


class Model(dict, metaclass=ModelMetaClass):
    def __init__(self, *args, **kwargs):
        super(Model, self).__init__(*args, **kwargs)
        self.request_data = None
        self.request_headers = None
        self.request_url = None

    # def __getattr__(self, key):
    #     try:
    #         return self[key]
    #     except KeyError:
    #         raise AttributeError(r"%s object has no attribute %s" % self.__class__.__name__, key)
    #
    # def __setattr__(self, key, value):
    #     self[key] = value

    def as_view(self):
        response = self.dispatch()
        return response

    def get_request_data(self):
        request_data = self.__mappings__['params'].data
        if isinstance(request_data, dict):
            request_data = json.dumps(request_data)
            self.request_data = request_data

    def update_request_data(self, data):
        if isinstance(data, dict):
            pass
        else:
            raise TypeError("data must be a dict!")

    def reset_request_data(self):
        pass

    def get_request_header(self):
        request_headers = self.__mappings__['headers'].data
        if not isinstance(request_headers, dict):
            raise TypeError("headers must be a dict type!")
        self.request_headers = request_headers

    def get_request_url(self):
        requests_url = self.__mappings__['url'].data
        if requests_url is None:
            raise Exception("you must set api url in interface instance class!")
        self.request_url = requests_url

    def _request_post(self):
        response = requests.post(url=self.request_url, data=self.request_data, headers=self.request_headers)
        return response

    def _request_get(self):
        response = requests.get(url=self.request_url, data=self.request_data, headers=self.request_headers)
        return response

    def dispatch(self):
        # 设置请求参数
        self.get_request_data()

        # 设置请求headers
        self.get_request_header()

        # 设置请求地址
        self.get_request_url()

        get_request_response = self._request_get()
        if get_request_response.status_code == 200:
            return get_request_response

        post_request_response = self._request_post()
        if post_request_response.status_code == 200:
            return post_request_response

        raise Exception("connect %s fails!" % self.get_request_url())