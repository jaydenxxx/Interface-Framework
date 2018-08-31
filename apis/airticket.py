from slwy_rest_framework.fields import ParamField
from slwy_rest_framework.models import PostAPI


class DomesticTicketFlight(PostAPI):
    data = {"data": {"arrCity": "CTU", "fromCity": "SHA", "takeOffDate": "2018-09-21 00:00:00", "fromCityName": "上海",
                     "arrCityName": "成都"}, "partnerType": "04"}
    params = ParamField(data)

    class Meta:
        url = "http://172.17.1.249:34001/domesticticketflight/yx/querysingle/flightQuerySingle"
