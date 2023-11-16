import requests
import os
from requests.exceptions import HTTPError
from urllib.parse import urlparse
from dotenv import load_dotenv
import argparse


def shorten_link(long_url, api_key):
    bit_url = 'https://api-ssl.bitly.com/v4/shorten'

    params = {
        'long_url': long_url
    }

    headers = {
         'Authorization': f'Bearer {api_key}'
    }

    response = requests.post(bit_url, headers=headers, json=params)
    response.raise_for_status()

    return response.json()['link']


def count_clicks(bitlink_id, api_key):
    bit_url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink_id}/clicks/summary"

    params = {
            'unit': 'day',
            'units': 1
        }

    headers = {
             'Authorization': f'Bearer {api_key}'
        }

    response = requests.get(bit_url, headers=headers, params=params)
    response.raise_for_status()

    return response.json()['total_clicks']


def is_bitlink(url, api_key):
    bit_url = f'https://api-ssl.bitly.com/v4/bitlinks/{url}'

    headers = {
             'Authorization': f'Bearer {api_key}'
        }

    response = requests.get(bit_url, headers=headers)

    return response.ok


def main():
    load_dotenv()
    apikey_bitly = os.getenv('APIKEY_BITLY')
    headers = {
        "Authorization": f"Bearer {apikey_bitly}",
    }
    parser = argparse.ArgumentParser(description='Сокращает ссылки и выводит количество переходов по ней')
    parser.add_argument('link', help='Введите ссылку:')
    args = parser.parse_args()
    parse_link = urlparse(args.link)
    bitlink = f"{parse_link.netloc}{parse_link.path}"
    try:
        if is_bitlink(headers, bitlink):
           print(count_clicks(headers, bitlink))
        else:
            print(shorten_link_url(headers, args.link))
    except requests.exceptions.HTTPError as error:
        print("Неверная ссылка.", error)


if __name__ == '__main__':
    main()
