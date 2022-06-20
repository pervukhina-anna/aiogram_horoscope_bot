import requests


def get_horoscope(endpoint, params):
    """Response to api service to get json data."""
    response = requests.post(endpoint, params=params)
    return response.json()
