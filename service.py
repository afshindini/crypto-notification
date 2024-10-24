"""Define service"""
import time
from typing import Any
from price import Coin, Zapier

def run_service(cfg: Any) -> None:
    """Create the service"""
    crypto = Coin(coin_name=cfg["CryptoInformation"]["name"],
                  coin_currency=cfg["CryptoInformation"]["currency"], 
                  base_url=cfg["CryptoInformation"]["api_url"],
                  api_key=cfg["CryptoInformation"]["api_key"])
    ifttt = Zapier(url=cfg["IFTTT"]["url"])
    while True:
        crypto.http_request()
        if crypto.response:
            price = crypto.get_latest_price()
            if price > cfg["Thresholds"]["upper_bound"] or price < cfg["Thresholds"]["lower_bound"]:
                timestamp = crypto.get_timestamp()
                ifttt.send_message(int(price), crypto.coin_currency, timestamp)
        time.sleep(cfg["Thresholds"]["message_cycle"]*60)
    