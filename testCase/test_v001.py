from apis import airticket
from slwy_rest_framework.testModel import CaseViewSet
import json



class est_v001(CaseViewSet):
    api = airticket.DomesticTicketFlight

    def test_v001(self):
        result_dict = json.loads(self.response.text)
        airCodeList = []

        for items in result_dict['data']['flights']:
            airCodeList.append(items['airCode'])

        assert "CA" in set(airCodeList)
        print(airCodeList)


if __name__ == '__main__':
    result = est_v001().test_v001()
    print(result)