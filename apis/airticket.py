from slwy_rest_framework.fields import ParamField, UrlField
from slwy_rest_framework.models import Model


class DomesticTicketFlight(Model):

    data = {"data": {"arrCity": "CTU", "fromCity": "SHA", "takeOffDate": "2018-09-21 00:00:00", "fromCityName": "上海",
                     "arrCityName": "成都"}, "partnerType": "04"}
    params = ParamField(data)
    url = UrlField("http://172.17.1.249:34001/domesticticketflight/yx/querysingle/flightQuerySingle")
