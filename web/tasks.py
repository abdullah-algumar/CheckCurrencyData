from web.serializers import CoinSerializer
from core.celery import app
from web.services import CollectCoinService

@app.task
def fetch_currency_data():
    service = CollectCoinService()
    data = service.collect_coins_data()
    if data is not None:
        serializer = CoinSerializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()