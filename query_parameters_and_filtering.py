# Task 2.2: Query Parameters and Filtering (5 points)
# Create functions that work with query parameters:

import requests
from requests.exceptions import HTTPError

def fetch_with_pagination(base_url, page=1, limit=10):
    """
    Fetch data with pagination parameters
    URL format: base_url?_page=<page>&_limit=<limit>
    Return: list of items
    """
    try:
        response = requests.get(base_url, params={"_page":page, "_limit":limit})
        response.raise_for_status()
        return response.json()
    except HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return []

def fetch_filtered_data(base_url, filters):
    """
    Fetch data with multiple filter parameters
    filters is a dict like: {'userId': 1, 'completed': True}
    Build query string from filters
    Return: list of filtered items
    """
    try:
        response = requests.get(base_url, params=filters)
        response.raise_for_status()
        return response.json()
    except HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return []

def fetch_sorted_data(base_url, sort_by, order='asc'):
    """
    Fetch data with sorting
    sort_by: field name to sort by
    order: 'asc' or 'desc'
    URL format: base_url?_sort=<field>&_order=<order>
    Return: sorted list of items
    """
    try:
        response = requests.get(base_url, params={"_sort":sort_by, "_order":order})
        response.raise_for_status()
        return response.json()
    except HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return []