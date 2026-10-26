import requests

API_URL = "https://api.api-ninjas.com/v1/dadjokes"


def generate_joke(api_key: str) -> str:
    headers = {"X-Api-Key": api_key}

    response = requests.get(API_URL, headers=headers)
    if requests.codes.ok == response.status_code:
        return response.json()[0]["joke"]

    # Fall back to a default joke if the API fails
    return "Time flies like an arrow. Fruit flies like a banana."
