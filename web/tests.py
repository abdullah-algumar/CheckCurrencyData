from unittest import TestCase
from unittest.mock import patch
from web.services import CollectCoinService
from web.serializers import CoinSerializer
import datetime
import zoneinfo


class CoinSerializerTestCase(TestCase):
    def test_get_serializer_action(self):
        data = {
            "name": "Dolar",
            "code": "BTC",
            "buying": 50000,
            "buyingstr": "50,000",
            "selling": 51000,
            "sellingstr": "51,000",
            "rate": 1000,
            "time": "10:00:00",
            "date": "2023-08-15",
            "datetime": "2023-08-15 10:00:00",
            "calculated": 1,
        }

        serializer = CoinSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data.get('name'), "Dolar")
        self.assertEqual(serializer.validated_data.get('code'), "BTC")
        self.assertEqual(serializer.validated_data.get('buying'), 50000)
        self.assertEqual(serializer.validated_data.get('buyingstr'), "50,000")
        self.assertEqual(serializer.validated_data.get('selling'), 51000)
        self.assertEqual(serializer.validated_data.get('sellingstr'), "51,000")
        self.assertEqual(serializer.validated_data.get('rate'), 1000)
        self.assertEqual(serializer.validated_data.get('time'), datetime.time(10, 0))
        self.assertEqual(serializer.validated_data.get('date'), datetime.date(2023, 8, 15))
        self.assertEqual(serializer.validated_data.get('datetime'), datetime.datetime(2023, 8, 15, 10, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC')))
        self.assertEqual(serializer.validated_data.get('calculated'), 1)


class MockResponse:
    def __init__(self, json_data, status_code):
        super().__init__()
        self.json_data = json_data
        self.status_code = status_code
        self.ok = 200 <= status_code < 300 

    def json(self):
        return self.json_data

class CollectCoinServiceTest(TestCase):
    collect_service = CollectCoinService()
    
    @patch('web.services.requests.get')
    def test_collect_coins_data(self, mock_get):
        mock_response = {
            'result': [{
            'name': 'Amerikan Doları',
            'code': 'USD',
            'buying': 27.056,
            'buyingstr': '27,0560',
            'selling': 27.0717,
            'sellingstr': '27,0717',
            'rate': 0.21,
            'time': '23:26',
            'date': '2023-08-15',
            'datetime': '2023-08-15T20:26:00.000Z',
            'calculated': 0
            }]
        }
        mock_get.return_value.ok = True
        mock_get.return_value.json.return_value = mock_response

        service = CollectCoinService()
        result = service.collect_coins_data()

        self.assertEqual(result, mock_response['result'])

    @patch('web.services.requests.get')
    def test_collect_coins_data_failure(self, mock_get):
        
        mock_response = MockResponse(json_data=None, status_code=404)
        mock_get.return_value = mock_response

        coins_data = self.collect_service.collect_coins_data()
        self.assertIsNone(coins_data)
