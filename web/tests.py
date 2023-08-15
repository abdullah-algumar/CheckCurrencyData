from unittest import mock, TestCase
import unittest
from web.services import CollectCoinService
from web.serializers import CoinSerializer


class CoinSerializerTestCase(TestCase):
    def test_get_serializer_action(self):
        data = {
            "name": "Dolar",
            "code": "BTC",
            "buying": 50000,
            "buying_str": "50,000",
            "selling": 51000,
            "selling_str": "51,000",
            "rate": 1000,
            "time": "10:00",
            "date": "2023-08-15",
            "datetime": "2023-08-15 10:00:00",
            "calculated": 1,
        }

        serializer = CoinSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data.get('name'), "Dolar")
        self.assertEqual(serializer.validated_data.get('code'), "BTC")
        self.assertEqual(serializer.validated_data.get('buying'), 50000)
        self.assertEqual(serializer.validated_data.get('buying_str'), "50,000")
        self.assertEqual(serializer.validated_data.get('selling'), 51000)
        self.assertEqual(serializer.validated_data.get('selling_str'), "51,000")
        self.assertEqual(serializer.validated_data.get('rate'), 1000)
        self.assertEqual(serializer.validated_data.get('time'), "10:00")
        self.assertEqual(serializer.validated_data.get('date'), "2023-08-15")
        self.assertEqual(serializer.validated_data.get('datetime'), "2023-08-15 10:00:00")
        self.assertEqual(serializer.validated_data.get('calculated'), 1)
        


class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

class CollectCoinServiceTest(TestCase):
    def setUp(self):
        self.collect_service = CollectCoinService()

    @mock.patch('requests.get')
    def test_collect_coins_data_success(self, mock_get):
        mock_response_data = [
            {
            "name": "Dolar",
            "code": "BTC",
            "buying": 50000,
            "buying_str": "50,000",
            "selling": 51000,
            "selling_str": "51,000",
            "rate": 1000,
            "time": "10:00",
            "date": "2023-08-15",
            "datetime": "2023-08-15 10:00:00",
            "calculated": 1,
        }
        ]

        mock_response = MockResponse(json_data=mock_response_data, status_code=200)
        mock_get.return_value = mock_response

        coins_data = self.collect_service.collect_coins_data()
        self.assertIsNotNone(coins_data)
        self.assertEqual(len(coins_data), len(mock_response_data))

        for expected_coin, actual_coin in zip(mock_response_data, coins_data):
            self.assertEqual(expected_coin['name'], actual_coin['name'])
            self.assertEqual(expected_coin['code'], actual_coin['code'])
            self.assertEqual(expected_coin['buying'], actual_coin['buying'])
            self.assertEqual(expected_coin['buying_str'], actual_coin['buying_str'])
            self.assertEqual(expected_coin['selling'], actual_coin['selling'])
            self.assertEqual(expected_coin['selling_str'], actual_coin['selling_str'])
            self.assertEqual(expected_coin['rate'], actual_coin['rate'])
            self.assertEqual(expected_coin['time'], actual_coin['time'])
            self.assertEqual(expected_coin['date'], actual_coin['date'])
            self.assertEqual(expected_coin['datetime'], actual_coin['datetime'])
            self.assertEqual(expected_coin['calculated'], actual_coin['calculated'])



    @mock.patch('requests.get')
    def test_collect_coins_data_failure(self, mock_get):
        mock_response = MockResponse(json_data=None, status_code=404)
        mock_get.return_value = mock_response

        coins_data = self.collect_service.collect_coins_data()
        self.assertIsNone(coins_data)

if __name__ == '__main__':
    unittest.main()


