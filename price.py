"""Python file to get the coin price"""
from dataclasses import dataclass, field
from typing import Any, Optional
import requests

import logging

logging.basicConfig(format="LOGGER:[{levelname}] {asctime} - {message}", style="{", datefmt="%Y-%m-%d %H:%M:%S")


@dataclass
class Coin:
    """Class to get the coin price"""
    coin_name:str = field(default='BTC')
    coin_currency: str = field(default='USD')
    base_url:str = field(default='https://rest.coinapi.io/v1/exchangerate/')
    api_key:str = field(default='E6166882-8300-4E1A-940F-207569236FB4')
    response: Optional[Any] = field(init=False, default=None)

    def __post_init__(self) -> None:
        """Post init method"""
        self.headers = {
            "X-CoinAPI-Key": self.api_key
        }
        self.endpoint = self.base_url + f'{self.coin_name}/' + f'{self.coin_currency}/'
    
    def http_request(self) -> None:
        """Make a GET request to the url"""
        data = requests.get(self.endpoint, headers=self.headers)
        if data.status_code == 403:
            logging.warning("Access to the requested resource is forbidden.")
            self.response = None
        elif data.status_code == 404:
            logging.warning("The requested page is not available.")
            self.response = None
        else:
            if 'rate' and 'time' not in data.json().keys():
                self.response = None
            else:
                self.response = data.json()
    
    def get_latest_price(self) -> float:
        """Get latest coin price"""
        return self.response['rate']
    
    def get_timestamp(self) -> str:
        """Return the timestamp of latest price"""
        return  self.response['time'].replace("T", " ").split(".")[0].replace(":", ".")

@dataclass
class Zapier:
    """Class to use as IFTTT with Zapier"""
    url: str = field(default='https://hooks.zapier.com/hooks/catch/20469947/210qssu/')
    
    def send_message(self, value:float, currency:str, timestamp:str) -> None:
        """Send meesage to the IFTTT Zapier"""
        data = {'Value1': value, 'Value2':currency, 'Value3':timestamp}
        requests.post(self.url, json=data)
        