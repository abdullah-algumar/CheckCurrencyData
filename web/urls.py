from django.urls import path
from .views import CoinListApiView

urlpatterns = [
    path("api/coins/", CoinListApiView.as_view(), name="coin-list")
]
