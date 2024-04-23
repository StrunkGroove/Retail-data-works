import time
from dataclasses import dataclass

import requests


@dataclass
class Good:
    item_id: int
    title: str
    webpage: str
    brand_name: str
    town: str


class ParsingItems4lapy:
    def __init__(self, token: str, authorization: str, cities: dict[str, str], 
                 extra_params: list[dict], category_id: str):
        # Data
        self._data = {}

        # Auth
        self._token = token
        self._authorization = authorization
        
        # Fetch const
        self._category_id = category_id
        self._url = 'https://4lapy.ru/api/v2/catalog/product/list/'
        self._delay = 5 # sec
        self._error_delay = 30 # sec

        # Parameters for fetches
        self._cities = cities
        self._extra_params = extra_params

    def main(self) -> dict[int, Good]:
        self._fetches()
        return self._data

    def _fetches(self) -> None:
        for city_name, city_number in self._cities.items():
            for data in self._extra_params:
                self._fetch(city_name, city_number, data)

    def _fetch(self, city_name: str, city_number: str, data: dict) -> None:
        while True:
            response = requests.get(
                self._url,
                headers=self._headers(city_number),
                params={**self._params(), **data}
            )
            try:
                response.raise_for_status()
            except requests.RequestException:
                print("Retrying...")
                time.sleep(self._error_delay)
            else:
                self._process_items(city_name, items=response.json())
                time.sleep(self._delay)
                break

    def _process_items(self, city: str, items: dict) -> None:
        for item in items['data']['goods']:
            self._data['{}-{}'.format(item['id'], city)] = Good(
                item_id=item['id'],
                title=item['title'], 
                webpage=item['webpage'],
                brand_name=item['brand_name'],
                town=city,
            )

    def _params(self) -> dict[str, str]:
        return {
            'category_id': self._category_id,
            'sort': 'popular',
            'token': self._token
        }

    def _headers(self, city: str) -> dict[str, str]:
        return {
            'Host': '4lapy.ru',
            'Cookie': f'selected_city_code={city}',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': self._authorization,
        }


class ParsingAdditionalInfo4lapy:
    def __init__(self, token: str, authorization: str, 
                 cities: dict[str, str], payloads: list[str]):
        # Data
        self._data = {}

        # Auth
        self._token = token
        self._authorization = authorization
        
        # Fetch const
        self._url = 'https://4lapy.ru/api/v2/catalog/product/info-list/'
        self._delay = 5 # sec
        self._error_delay = 30 # sec
        
        # Parameters for fetches
        self._cities = cities
        self._payloads = payloads

    def main(self) -> dict[int, float]:
        self._fetches()
        return self._data

    def _fetches(self) -> None:
        for city_name, city_number in self._cities.items():
            for payload in self._payloads:
                self._fetch(city_name, city_number, payload)
    
    def _fetch(self, city_name: str, city_number: str, payload: str) -> None:
        while True:
            response = requests.post(
                self._url,
                headers=self._headers(city_number),
                data=payload
            )
            try:
                response.raise_for_status()
            except requests.RequestException:
                print("Retrying...")
                time.sleep(self._error_delay)
            else:
                self._process(city_name, response.json())
                time.sleep(self._delay)
                break

    def _process(self, city: str, items: dict) -> None:
        for item in items['data']['products']:
            element = item['variants'][0]
            if element['active'] != True: continue # check if the item is in stock
            price = element['price']['actual']
            self._data['{}-{}'.format(element['id'], city)] = price

    def _headers(self, city: str) -> dict[str, str]:
        return {
            'Host': '4lapy.ru',
            'Cookie': f'selected_city_code={city}',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': self._authorization,
            'Accept-Encoding': 'utf-8',
        }