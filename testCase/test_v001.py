from apis import airticket
import json


class Test_v001:
    def test_v001(self):
        result = airticket.DomesticTicketFlight().as_view()
        result_dict = json.loads(result.text)
        airCodeList = []

        for items in result_dict['data']['flights']:
            airCodeList.append(items['airCode'])

        assert "CA" in set(airCodeList)
        pass
