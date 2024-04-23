## Task
Super Hard. Написать парсер для мобильного приложения 4 лапы (https://4lapy.ru/shares/mobilnoe-prilozhenie-chetyre-lapy/) 
Важно! Парсер должен использовать ТОЛЬКО те эндпоинты, которые использует мобильное приложение 4 лап. Если же их не получается достать, например, исследованием сетевого трафика, то выбирайте другое задание.

Для каждой торговой площадки требования одни и те же. Спарсить любую категорию, где более 100 товаров, для городов Москва и Санкт-Петербург и выгрузить в любой удобный формат(csv, json, xlsx). Важно, чтобы товары были в наличии.

Необходимые данные: 
- id товара из сайта/приложения, 
- наименование, 
- ссылка на товар, 
- регулярная цена, 
- промо цена, 
- бренд
    
## Info
В разработке использовал проксирование с помощью Burp Suite. 

## For start
### Download
```
git clone https://github.com/StrunkGroove/Retail-data-works.git && cd Retail-data-works
```
### Create virtual env and activate
```
python -m venv venv && source venv/bin/activate
```
### Install req
```
pip install -r requirements.txt
```
### Start
```
python main.py
```
