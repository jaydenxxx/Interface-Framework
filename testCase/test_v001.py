from apis import airticket
import json


class est_v001:
    def test_v001(self):
        result = airticket.DomesticTicketFlight().as_view()
        result_dict = json.loads(result.text)
        airCodeList = []

        for items in result_dict['data']['flights']:
            airCodeList.append(items['airCode'])

        assert "CA" in set(airCodeList)


if __name__ == '__main__':
    result = est_v001().test_v001()
    print(result)