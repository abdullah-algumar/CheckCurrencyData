import os
import requests

from web.serializers import CoinSerializer

class CollectCoinService:
    base_url = os.environ.get('BASE_URL')
    headers = {
        'content-type': "application/json",
        'authorization': os.environ.get('API_KEY')
    }

    def collect_coins_data(self):
        response = requests.get(f"{self.base_url}/economy/allCurrency", headers=self.headers)
        if response.ok:
            json_response = response.json()
            data = json_response['result']
            serializer = CoinSerializer(data=data, many=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return json_response['result']

        return None