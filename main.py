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
    api_key = os.getenv('API_KEY')
    long_url = input('Введите ссылку: ')
    parsed_url = urlparse(long_url)
    combined_path = f"{parsed_url.netloc}{parsed_url.path}"

    try:
        if is_bitlink(combined_path, api_key):
            print(count_clicks(combined_path, api_key))
        else:
            print(shorten_link(long_url, api_key))
    except HTTPError as error:
        print("Неправильная ссылка: ", error)

if __name__ == '__main__':
    main()