"""Get words similar to a word in an aspect.

Use datamuse api to get words similar to a given word in a specified aspect.

Example:
    $ synonyms('Hello')

Todo:
    * Lookup for improvements and apply them.
"""
import requests


def request(url: str = None, parameters: dict = None) -> requests.Response:
    """Get a response from any website with the passed parameters.

    Args:
        url (str, optional): URL of the website to request from it.  If not specified, the user will be prompted for it. Defaults to None.
        parameters (dict, optional): Parameters to pass to the website. If not specified, the user will be prompted for it. Defaults to None.

    Returns:
        requests.Response: Website's response.
    """

    if url == None:
        url = input('Enter a url to fetch the data from: ')
    if parameters == None:
        parameters = input('Enter the parameters. Separate the key and the value with :, and the pairs with ;, any spaces will be ignored:\n')
        parameters = {key:value for key,value in (item.split(':') for item in parameters.replace(' ', '').split(';'))}

    return requests.get(url, params=parameters)


def datamuse_call(parameters: dict = None) -> dict:
    """A function that call Datamuse API, and return the value. Here is its documentations: https://www.datamuse.com/api/

    Args:
        parameters (dict, optional): Parameters to pass to datamuse API. If not specified, the user will be prompted for it. Defaults to None.

    Returns:
        dict: A dictionary of the response
    """
    
    baseURL = 'https://api.datamuse.com/words'
    response = request(baseURL, parameters)
    return response.json()


def meaning(word: str) -> list[str]:
    """Search for words that has a similar meaning of the passed word.

    Args:
        word (str): Word to search with.

    Returns:
        list[str]: A list of words that has a similar meaning.
    """
    response = datamuse_call({'ml': word})
    if len(response) == 0:
        return ['No results.']
    return [x['word'] for x in response]


def sound(word: str) -> list[str]:
    """Search for words that has a similar sound of the passed word.

    Args:
        word (str): Word to search with.

    Returns:
        list[str]: A list of words that has a similar sound.
    """
    response = datamuse_call({'sl': word})
    if len(response) == 0:
        return ['No results.']
    return [x['word'] for x in response]


def spelling(word: str) -> list[str]:
    """Search for words that has a similar spelling of the passed word.

    Args:
        word (str): Word to search with.

    Returns:
        list[str]: A list of words that has a similar spelling.
    """
    response = datamuse_call({'sp': word})
    if len(response) == 0:
        return ['No results.']
    return [x['word'] for x in response]


def synonyms(word: str) -> list[str]:
    """Search for synonyms of the passed word.

    Args:
        word (str): Word to search with.

    Returns:
        list[str]: A list of synonyms.
    """
    response = datamuse_call({'rel_syn': word})
    if len(response) == 0:
        return ['No results.']
    return [x['word'] for x in response]


def antonyms(word: str) -> list[str]:
    """Search for antonyms of the passed word.

    Args:
        word (str): Word to search with.

    Returns:
        list[str]: A list of antonyms.
    """
    response = datamuse_call({'rel_ant': word})
    if len(response) == 0:
        return ['No results.']
    return [x['word'] for x in response]


def adj_of_noun(word: str) -> list[str]:
    """Search for adjectives of the passed word.

    Args:
        word (str): Word to search with.

    Returns:
        list[str]: A list of adjectives.
    """
    response = datamuse_call({'rel_jjb': word})
    if len(response) == 0:
        return ['No results.']
    return [x['word'] for x in response]


def kinds(word: str) -> list[str]:
    """Search for the kinds of the passed word.

    Args:
        word (str): Word to search with.

    Returns:
        list[str]: A list of the kinds.
    """
    response = datamuse_call({'rel_spc': word})
    if len(response) == 0:
        return ['No results.']
    return [x['word'] for x in response]


def requestURL(baseurl: str, params: dict = {}):
    """For debugging APIs' responses.

    Args:
        baseurl (str): URL of the website to test.
        params (dict, optional): Parameters to pass to the website. Defaults to {}.

    Returns:
        str: The full url with the parameters.
    """
    req = requests.Request(method = 'GET', url = baseurl, params = params)
    prepped = req.prepare()
    return prepped.url


if __name__ == '__main__':
    word = input('* ')

    # print(meaning(word)[:5])
    # print(sound(word)[:5])
    # print(spelling(word)[:5])
    # print(synonyms(word)[:5])
    print(antonyms(word)[:5])
    # print(adj_of_noun(word)[:5])
    # print(kinds(word)[:5])