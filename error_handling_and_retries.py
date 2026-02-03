# Task 2.3: Error Handling and Retries (10 points)
# Create robust API functions with error handling:

import time
import requests

def make_request_with_retry(url, max_retries=3, delay=1):
    """
    Make a GET request with retry logic
    Retry on network errors and 5xx status codes
    Wait 'delay' seconds between retries
    Return: response object or None if all retries fail
    Print retry attempts
    """
    pass

def fetch_with_timeout(url, timeout=5):
    """
    Make a request with timeout
    Handle timeout exception gracefully
    Return: (success: bool, data/error_message)
    """
    try:
        r = requests.get(url, timeout=timeout)
        r.raise_for_status()
        return (True, r.json())
    except requests.Timeout as e:
        print(e)
        return (False, "Request timed out!")
    except requests.RequestException as e:
        print(e)
        return (False, str(e))
    except ValueError as e:
        print(e)
        return (False, "Invalid JSON response")


def safe_api_call(func):
    """
    Decorator that wraps API calls with error handling
    Catches: requests.exceptions.RequestException, ValueError, KeyError
    Prints error message and returns None on failure
    
    Usage:
        @safe_api_call
        def get_data():
            return requests.get(url).json()
    """
    pass