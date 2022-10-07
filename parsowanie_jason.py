import json

from pprint import pprint
import requests

SZABLON_URL = 'http://api.nbp.pl/api/exchangerates/rates/a/{}/2016-04-04/?format=json'


# def policz_koszyk(koszyk):
#     suma = 0
#     for waluta, ilosc in koszyk.items():
#         url = SZABLON_URL.format(waluta)
#         r = requests.get(url)
#         r.raise_for_status()
#         j = r.json()
#         kwota = j['rates'][0]['mid'] * ilosc
#         suma += kwota
#     return suma
#
#
# def policz_koszyk_lepiej(koszyk):
#     suma = 0
#     for waluta, ilosc in koszyk.items():
#         url = SZABLON_URL.format(waluta)
#         r = requests.get(url)
#         r.raise_for_status()
#         j = r.json()
#         kwota = j['rates'][0]['mid'] * ilosc
#         suma += kwota
#     return suma
#
#
# if __name__ == '__main__':
#     k = {
#         'usd': 34,
#         'chf': 200,
#         'eur': 555
#     }
#     print('Wartosc koszyka: ', policz_koszyk(k))


    # lub



def policz_koszyk(koszyk):
    suma = 0
    for waluta, ilosc in koszyk.items():
        url = SZABLON_URL.format(waluta)
        r = requests.get(url)
        r.raise_for_status()
        j = r.json()
        kwota = j['rates'][0]['mid'] * ilosc
        suma += kwota
    return suma


def policz_koszyk_lepiej(koszyk):
    suma = 0
    url = 'https://api.nbp.pl/api/exchangerates/tables/a/?format=json'
    r = requests.get(url)
    r.raise_for_status()
    j = r.json()
    kursy = {d['code'].lower(): d['mid'] for d in j[0]['rates']}
    pprint(kursy)
    for waluta, ilosc in koszyk.items():
        kwota = kursy[waluta.lower()] * ilosc
        suma += kwota
    return suma


if __name__ == '__main__':
    k = {
        'usd': 34,
        'chf': 200,
        'eur': 555
    }
    print('Wartosc koszyka: ', policz_koszyk_lepiej(k))
