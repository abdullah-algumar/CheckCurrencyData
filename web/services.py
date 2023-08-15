import requests

class CollectCoinService:
    base_url = "api.collectapi.com"
    headers = {
        'content-type': "application/json",
        'authorization': "apikey 1EaWYnZdhXA3mpX9xPv2ay:3csfSMofNMLynsn2FTOpL2"
    }

    def collect_coins_data(self):
        response = requests.get(f"{self.base_url}/economy/allCurrency", headers=self.headers)
        if response.ok:
            json_response = response.json()
            return json_response

        return None