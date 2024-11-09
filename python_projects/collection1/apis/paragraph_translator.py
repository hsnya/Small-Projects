"""Exploring some APIs.

_Description_.

Example:
    $ python example_google.py

Section.

Attributes:
    module_level_variable1 (int): Description.

Todo:
    * Complete the paragraph translator
    * Lookup for improvements and apply them.
"""
import copy
import json

import requests


def datamuse(parameters: dict = None) -> dict:
    """A function that uses Datamuse API. Here is its documentations : https://www.datamuse.com/api/"""
    
    if parameters == None:
        parameters = input('Enter the parameters. Separate the key and the value with :, and the pairs with ;, any spaces will be ignored:\n')
        parameters = {key:value for key,value in (item.split(':') for item in parameters.replace(' ', '').split(';'))}

    response = requests.get('https://api.datamuse.com/words', params=parameters)
    return json.loads(response.text)


def translate_paragraph(paragraph):
    return paragraph


def fetch_response(url: str = None, parameters: dict = None) -> requests.Response:
    """A function that fetch a general response to any website with the passed parameters."""

    if url == None:
        url = input('Enter a url to fetch the data from: ')
    if parameters == None:
        parameters = input('Enter the parameters. Separate the key and the value with :, and the pairs with ;, any spaces will be ignored:\n')
        parameters = {key:value for key,value in (item.split(':') for item in parameters.replace(' ', '').split(';'))}

    return requests.get(url, params=parameters)


def requestURL(baseurl, params = {}):
    # This function accepts a URL path and a params diction as inputs.
    # It calls requests.get() with those inputs,
    # and returns the full URL of the data you want to get.
    req = requests.Request(method = 'GET', url = baseurl, params = params)
    prepped = req.prepare()
    return prepped.url


if __name__ == '__main__':
    baseurl = 'http://api.icndb.com/jokes/random'
    response = requests.get(baseurl, params={'limitTo': ['nerdy']})
    print(requests.Request(method = 'GET', url = baseurl, params = {'limitTo': ['nerdy']}).prepare().url)