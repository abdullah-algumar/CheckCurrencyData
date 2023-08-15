from django.test import TestCase
from web.serializers import CoinSerializer


class CoinSerializerTestCase(TestCase):
    def test_get_serializer_action(self):
        data = {
            "name": "Dolar"
        }

        serializer = CoinSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertTrue(data.get('name') in serializer.validated_data)