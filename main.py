import json

from data import (
    TOKEN, AUTHORIZATION, CATEGORY_ID, CITIES, PARSING_ELEMENTS, PRICES_PAYLOAD
)
from services import Good, ParsingItems4lapy, ParsingAdditionalInfo4lapy


class Main:
    def __init__(self, output_file_path='./data.json'):
        self._data = []
        self._output_file_path = output_file_path

    def main(self, token: str, authorization: str, cities: dict[str, str], 
             category_id: str, parsing_elements: list[dict], 
             prices_payload: list[str]) -> None:
        elements = ParsingItems4lapy(
            token=token, 
            authorization=authorization,
            cities=cities,
            extra_params=parsing_elements,
            category_id=category_id
        ).main()
        prices = ParsingAdditionalInfo4lapy(
            token=token,
            authorization=authorization,
            cities=cities, 
            payloads=prices_payload
        ).main()
        self._merge(elements, prices)
        self._save()

    def _merge(self, elements: dict[int, Good], prices: dict[int, float]) -> None:
        for item_id, element in elements.items():
            price = prices.get(item_id)
            if price is not None:
                self._data.append({
                    **element.__dict__,
                    'price': price,
                    'price_with_sale': price
                })

    def _save(self) -> None:
        with open(self._output_file_path, "w") as f:
            json.dump(self._data, f, indent=4)
        print(f'Saved: {len(self._data)} elements')

if __name__ == "__main__":
    Main().main(
        token=TOKEN,
        authorization=AUTHORIZATION,
        cities=CITIES,
        category_id=CATEGORY_ID,
        parsing_elements=PARSING_ELEMENTS,
        prices_payload=PRICES_PAYLOAD
    )
