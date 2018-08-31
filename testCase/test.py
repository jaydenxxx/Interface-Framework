from slwy_rest_framework.models import PostAPI
from slwy_rest_framework.fields import ParamField

class LoginAPI(PostAPI):
    params = {
        "loginName": "13982228044",
        "userPassword": "E10ADC3949BA59ABBE56E057F20F883E",
        "partnerCode": 1,
        "partnerType": "04"
    }
    params = ParamField(params)

    class Meta:
        url = "http://172.17.1.249:34007/cuser/cuserinfo/login"


if __name__ == '__main__':
    login = LoginAPI()
    response = login.as_view()
    print(response.text)