import os
import requests
from dotenv import load_dotenv


API_URL = "https://world.openfoodfacts.org/api/v2/product/"
CONNECT_TIMEOUT = 5  # seconds
READ_TIMEOUT = 10  # seconds
ENCODING = "utf-8"


def get_product_info(barcode):
    try:
        # Load environment variables from .env
        load_dotenv()
        response = requests.get(f"{API_URL}{barcode}.json",
                                timeout=(CONNECT_TIMEOUT, READ_TIMEOUT))
        response.encoding = ENCODING
        data = response.json()

        # Check if API response was successful
        if data.get("Response") == "False":
            print(f"API error: {data.get('Error', 'Unknown error')}")
            return None

        return data
    except requests.exceptions.Timeout:
        print("The API request timed out")
    except (KeyError, IndexError, ValueError) as error:
        print(f"Data parsing error: {error}")
    except requests.RequestException as error:
        print(f"Request error: {error}")
    return None
