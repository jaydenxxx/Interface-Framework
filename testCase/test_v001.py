from apis import airticket
from slwy_rest_framework.testModel import ModelCase
import json


class Test_v001_apiname(ModelCase):
    """
    v001版本机票查询接口
    """
    api = airticket.DomesticTicketFlight

    # 用例1
    def test_v001(self):
        """
        航班查询中是否有CA航司
        :return:
        """
        result_dict = json.loads(self.response.text)
        airCodeList = []

        for items in result_dict['data']['flights']:
            airCodeList.append(items['airCode'])

        assert "CA" in set(airCodeList)
        print(airCodeList)

    def test_v003(self):
        result_dict = json.loads(self.response.text)
        airCodeList = []

        for items in result_dict['data']['flights']:
            airCodeList.append(items['airCode'])

        assert "CA" in set(airCodeList)
        print(airCodeList)

    def test_v004(self):
        result_dict = json.loads(self.response.text)
        airCodeList = []

        for items in result_dict['data']['flights']:
            airCodeList.append(items['airCode'])

        assert "CA" in set(airCodeList)
        print(airCodeList)

    # 用例2
    def test_v002(self):
        # 重置入参
        data = {
            "data": {"arrCity": "PEK", "fromCity": "SHA", "takeOffDate": "2018-09-21 00:00:00", "fromCityName": "上海",
                     "arrCityName": "北京"}, "partnerType": "04"}
        self.api().reset_request_data(data)

        result_dict = json.loads(self.response.text)
        airCodeList = []

        for items in result_dict['data']['flights']:
            airCodeList.append(items['airCode'])

        assert "CA" in set(airCodeList)
        print(airCodeList)

# if __name__ == '__main__':
#     # est_v001().test_v001()
#     est_v001().test_v002()
#     pass
