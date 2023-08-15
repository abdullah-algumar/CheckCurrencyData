from rest_framework.generics import ListAPIView
from web.models import Coin
from web.serializers import CoinSerializer


class CoinListApiView(ListAPIView):
    queryset = Coin.objects.all().order_by('-created_at')
    serializer_class = CoinSerializer
    permission_classes = []