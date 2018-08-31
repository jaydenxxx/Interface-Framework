class Field:
    def __init__(self, data, **kwargs):
        self.data = data

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.data)


class Header(Field):
    def __init__(self, **kwargs):
        self.data = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json;charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 Safari/601.1 wechatdevtools/1.02.1808101 MicroMessenger/6.5.7 Language/zh_CN webview/15355365235235902 webdebugger port/62427",
        }
        super(Header, self).__init__(self.data, **kwargs)
        for k, v in kwargs.items():
            self.data[k] = v


# 登录类
class LoginField(Field):
    def __init__(self, data):
        super(LoginField, self).__init__(data=data)


# API入参类
class ParamField(Field):
    def __init__(self, data):
        super(ParamField, self).__init__(data=data)
