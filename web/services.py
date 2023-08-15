import os
import requests

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
            return json_response

        return None