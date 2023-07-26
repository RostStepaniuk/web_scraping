import requests
import os
import csv
import json
from datetime import datetime


def get_data():
    import requests

    cookies = {
        '__lhash_': '4efa187f2d8e63012b8f3635009ce312',
        'MVID_ALFA_PODELI_NEW': 'true',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CATALOG_STATE': '1',
        'MVID_CITY_ID': 'CityCZ_975',
        'MVID_CREDIT_SERVICES': 'true',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GIFT_KIT': 'true',
        'MVID_GTM_ENABLED': '011',
        'MVID_INTERVAL_DELIVERY': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '7700000000000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_MCLICK': 'true',
        'MVID_MINDBOX_DYNAMICALLY': 'true',
        'MVID_MINI_PDP': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_PODELI_PDP': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_REGION_ID': '1',
        'MVID_REGION_SHOP': 'S002',
        'MVID_SERVICES': '111',
        'MVID_SP': 'true',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_TYP_CHAT': 'true',
        'MVID_WEB_SBP': 'true',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        'MVID_ENVCLOUD': 'prod1',
        '_gid': 'GA1.2.1952803338.1690283438',
        'partnerSrc': 'google',
        '__SourceTracker': 'google__organic',
        'admitad_deduplication_cookie': 'google__organic',
        '__cpatrack': 'google_organic',
        '__sourceid': 'google',
        '__allsource': 'google',
        'SMSError': '',
        'authError': '',
        'flocktory-uuid': 'bf968713-6fdf-4d6a-9069-6bbbad14b45e-5',
        'afUserId': '02721a41-56d1-4c2d-8b24-58b87ab75e19-p',
        'AF_SYNC': '1690283442244',
        'uxs_uid': 'ebe0b280-2adb-11ee-a1db-233e38152e09',
        'adrdel': '1',
        'adrcid': 'AM75M66ZQDveNJcJe_iHEkQ',
        'flacktory': 'no',
        'BIGipServeratg-ps-prod_tcp80': '1912921098.20480.0000',
        'MVID_GUEST_ID': '22778409022',
        'MVID_VIEWED_PRODUCTS': '',
        'wurfl_device_id': 'generic_web_browser',
        'JSESSIONID': 'JKxYk1nPQQTKMFtsgllGbGcjdzWfdrQfhKnSCchFS7swSJjgKm1P!-1685884438',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'MVID_CART_MULTI_DELETE': 'true',
        'MVID_YANDEX_WIDGET': 'true',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'false',
        'HINTS_FIO_COOKIE_NAME': '1',
        'searchType2': '3',
        'COMPARISON_INDICATOR': 'false',
        'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
        'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
        'BIGipServeratg-ps-prod_tcp80_clone': '1912921098.20480.0000',
        'CACHE_INDICATOR': 'true',
        'MVID_GTM_BROWSER_THEME': '1',
        'deviceType': 'mobile',
        'BIGipServericerock-prod': '3187989514.20480.0000',
        'bIPs': '-957002303',
        '_ga_CFMZTSS5FM': 'GS1.1.1690290892.3.1.1690291410.0.0.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1690290892.3.1.1690291411.60.0.0',
        '_ga': 'GA1.2.557107506.1690283438',
        'gssc218': '',
        '__js_p_': '625,1800,0,1,0',
        '__rhash_': 'e7311ef72175223b1754fcb055895d7e',
        '__jhash_': '578',
        '__jua_': 'Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F114.0.0.0%20Safari%2F537.36',
        '__hash_': '8a4ea684e755323b175e47b56fe04a8d',
        'cfidsgib-w-mvideo': 'qAgL38O2dlHx2YHbV7cuULuuEVC5ls0h0K9D8pOfCVRu4URpH2RDDzLyGD6ZQKOZWKVgLwfuQkNwTlV+gIiqfSzHb2GVcIri9L8iG4NPvw1L6/ecDS7wyyAae2BAI/Nvqqe47ACNshqazBhaJpv0AdwnBzs3Sx2RaW1QWXE=',
        'gsscgib-w-mvideo': 'p9gsU6ovOUT28NODvIKd5Rj3nxu+PI1NOWkhSxv6wEVUbEQrOJ5mzSQlTU3EYF8O5ko9Z+cMXQEfvkow1u3579pdRyx6xGGWrZz1iSBBPRZGWtPaJPZayHw/exHdq+zXvXhzAu7lPu/BO0KPmZK73MS8jRwA1W5diZxdCdHaAIyXbx1u8Ukpw+NvB25imxvkHh9lb/9Ztf6J/Sb3tDPPWjzGvTkpfqLg9bxbTxfdcsEfu+vko2P9NDd0ENv5PxlaR78=',
        'gsscgib-w-mvideo': 'p9gsU6ovOUT28NODvIKd5Rj3nxu+PI1NOWkhSxv6wEVUbEQrOJ5mzSQlTU3EYF8O5ko9Z+cMXQEfvkow1u3579pdRyx6xGGWrZz1iSBBPRZGWtPaJPZayHw/exHdq+zXvXhzAu7lPu/BO0KPmZK73MS8jRwA1W5diZxdCdHaAIyXbx1u8Ukpw+NvB25imxvkHh9lb/9Ztf6J/Sb3tDPPWjzGvTkpfqLg9bxbTxfdcsEfu+vko2P9NDd0ENv5PxlaR78=',
        'fgsscgib-w-mvideo': 'WdO578385260c741061b37f0050944450ec92488',
        'fgsscgib-w-mvideo': 'WdO578385260c741061b37f0050944450ec92488',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'baggage': 'sentry-environment=production,sentry-transaction=%2F**%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=1f2ef790901d482cb39e97ec1d79b30d,sentry-sample_rate=0.5',
        'cache-control': 'no-cache',
        # 'cookie': '__lhash_=4efa187f2d8e63012b8f3635009ce312; MVID_ALFA_PODELI_NEW=true; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_975; MVID_CREDIT_SERVICES=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GIFT_KIT=true; MVID_GTM_ENABLED=011; MVID_INTERVAL_DELIVERY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7700000000000; MVID_LAYOUT_TYPE=1; MVID_MCLICK=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_NEW_ACCESSORY=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PODELI_PDP=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_SERVICES=111; MVID_SP=true; MVID_TIMEZONE_OFFSET=3; MVID_TYP_CHAT=true; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; MVID_ENVCLOUD=prod1; _gid=GA1.2.1952803338.1690283438; partnerSrc=google; __SourceTracker=google__organic; admitad_deduplication_cookie=google__organic; __cpatrack=google_organic; __sourceid=google; __allsource=google; SMSError=; authError=; flocktory-uuid=bf968713-6fdf-4d6a-9069-6bbbad14b45e-5; afUserId=02721a41-56d1-4c2d-8b24-58b87ab75e19-p; AF_SYNC=1690283442244; uxs_uid=ebe0b280-2adb-11ee-a1db-233e38152e09; adrdel=1; adrcid=AM75M66ZQDveNJcJe_iHEkQ; flacktory=no; BIGipServeratg-ps-prod_tcp80=1912921098.20480.0000; MVID_GUEST_ID=22778409022; MVID_VIEWED_PRODUCTS=; wurfl_device_id=generic_web_browser; JSESSIONID=JKxYk1nPQQTKMFtsgllGbGcjdzWfdrQfhKnSCchFS7swSJjgKm1P!-1685884438; MVID_CALC_BONUS_RUBLES_PROFIT=true; NEED_REQUIRE_APPLY_DISCOUNT=true; MVID_CART_MULTI_DELETE=true; MVID_YANDEX_WIDGET=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; MVID_GET_LOCATION_BY_DADATA=DaData; PRESELECT_COURIER_DELIVERY_FOR_KBT=false; HINTS_FIO_COOKIE_NAME=1; searchType2=3; COMPARISON_INDICATOR=false; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; BIGipServeratg-ps-prod_tcp80_clone=1912921098.20480.0000; CACHE_INDICATOR=true; MVID_GTM_BROWSER_THEME=1; deviceType=mobile; BIGipServericerock-prod=3187989514.20480.0000; bIPs=-957002303; _ga_CFMZTSS5FM=GS1.1.1690290892.3.1.1690291410.0.0.0; _ga_BNX5WPP3YK=GS1.1.1690290892.3.1.1690291411.60.0.0; _ga=GA1.2.557107506.1690283438; gssc218=; __js_p_=625,1800,0,1,0; __rhash_=e7311ef72175223b1754fcb055895d7e; __jhash_=578; __jua_=Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F114.0.0.0%20Safari%2F537.36; __hash_=8a4ea684e755323b175e47b56fe04a8d; cfidsgib-w-mvideo=qAgL38O2dlHx2YHbV7cuULuuEVC5ls0h0K9D8pOfCVRu4URpH2RDDzLyGD6ZQKOZWKVgLwfuQkNwTlV+gIiqfSzHb2GVcIri9L8iG4NPvw1L6/ecDS7wyyAae2BAI/Nvqqe47ACNshqazBhaJpv0AdwnBzs3Sx2RaW1QWXE=; gsscgib-w-mvideo=p9gsU6ovOUT28NODvIKd5Rj3nxu+PI1NOWkhSxv6wEVUbEQrOJ5mzSQlTU3EYF8O5ko9Z+cMXQEfvkow1u3579pdRyx6xGGWrZz1iSBBPRZGWtPaJPZayHw/exHdq+zXvXhzAu7lPu/BO0KPmZK73MS8jRwA1W5diZxdCdHaAIyXbx1u8Ukpw+NvB25imxvkHh9lb/9Ztf6J/Sb3tDPPWjzGvTkpfqLg9bxbTxfdcsEfu+vko2P9NDd0ENv5PxlaR78=; gsscgib-w-mvideo=p9gsU6ovOUT28NODvIKd5Rj3nxu+PI1NOWkhSxv6wEVUbEQrOJ5mzSQlTU3EYF8O5ko9Z+cMXQEfvkow1u3579pdRyx6xGGWrZz1iSBBPRZGWtPaJPZayHw/exHdq+zXvXhzAu7lPu/BO0KPmZK73MS8jRwA1W5diZxdCdHaAIyXbx1u8Ukpw+NvB25imxvkHh9lb/9Ztf6J/Sb3tDPPWjzGvTkpfqLg9bxbTxfdcsEfu+vko2P9NDd0ENv5PxlaR78=; fgsscgib-w-mvideo=WdO578385260c741061b37f0050944450ec92488; fgsscgib-w-mvideo=WdO578385260c741061b37f0050944450ec92488',
        'pragma': 'no-cache',
        'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/planshety-195/f/skidka=da/tolko-v-nalichii=da',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': '1f2ef790901d482cb39e97ec1d79b30d-a916423a74f7a25b-1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'x-gib-fgsscgib-w-mvideo': 'WdO578385260c741061b37f0050944450ec92488',
        'x-gib-gsscgib-w-mvideo': 'p9gsU6ovOUT28NODvIKd5Rj3nxu+PI1NOWkhSxv6wEVUbEQrOJ5mzSQlTU3EYF8O5ko9Z+cMXQEfvkow1u3579pdRyx6xGGWrZz1iSBBPRZGWtPaJPZayHw/exHdq+zXvXhzAu7lPu/BO0KPmZK73MS8jRwA1W5diZxdCdHaAIyXbx1u8Ukpw+NvB25imxvkHh9lb/9Ztf6J/Sb3tDPPWjzGvTkpfqLg9bxbTxfdcsEfu+vko2P9NDd0ENv5PxlaR78=',
        'x-set-application-id': 'e2ab28a5-4efb-4fb9-b738-1793c242344b',
    }

    params = {
        'categoryId': '195',
        'offset': '0',
        'limit': '24',
        'filterParams': [
            'WyJza2lka2EiLCIiLCJkYSJd',
            'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
        ],
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                            headers=headers).json()

    # print(response)

    products_ids = response.get('body').get('products')

    with open('1_products_ids.json', 'w') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)


    json_data = {
        'productIds': products_ids,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
                             json=json_data).json()
    with open('2_items.json', 'w', encoding='utf-8') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)









# узнать что делает эта хуйня
    products_ids_str = ','.join(products_ids)


    params = {
        'productIds': products_ids_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies,
                            headers=headers).json()

    with open('3_prices.json', 'w', encoding='utf-8') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    items_prices = {}

    material_prices = response.get('body').get('materialPrices')

    for item in material_prices:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_sale_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')

        items_prices[item_id] = {
            'item_basePrice': item_base_price,
            'item_salePrice': item_sale_price,
            'item_bonus': item_bonus
        }

    with open('4_items_prices.json', 'w', encoding='utf-8') as file:
        json.dump(items_prices, file, indent=4, ensure_ascii=False)



def get_result():
    with open('2_items.json', encoding='utf-8') as file:
        products_data = json.load(file)

    with open('4_items_prices.json', encoding='utf-8') as file:
        products_prices = json.load(file)

    product_data = products_data.get('body').get('products')

    for item in product_data:  # <-- Исправленное имя переменной
        product_id = item.get('productId')

        if product_id in products_prices:
            prices = products_prices[product_id]

            item['item_basePrice'] = prices.get('item_basePrice')
            item['item_salePrice'] = prices.get('item_salePrice')
            item['item_bonus'] = prices.get('item_bonus')

    with open('5_result.json', 'w', encoding='utf-8') as file:  # <-- Добавлено указание кодировки при записи
        json.dump(product_data, file, indent=4, ensure_ascii=False)



def main():
    get_data()
    get_result()


if __name__=='__main__':
    main()