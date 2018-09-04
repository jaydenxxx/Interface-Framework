from slwy_rest_framework.fields import ParamField, UrlField, AccountField
from slwy_rest_framework.models import Model


class DomesticTicketFlight(Model):
    # 入参
    data = {"data": {"arrCity": "CTU", "fromCity": "SHA", "takeOffDate": "2018-09-21 00:00:00", "fromCityName": "上海",
                     "arrCityName": "成都"}, "partnerType": "04"}
    params = ParamField(data)

    # 接口地址
    url = UrlField("http://172.17.1.249:34001/domesticticketflight/yx/querysingle/flightQuerySingle")

    # 登录账号（可选）
    account = AccountField(
        {"loginName": "18384591339",
         "userPassword": "E10ADC3949BA59ABBE56E057F20F883E",
         "partnerCode": 1,
         "partnerType": "04"})
