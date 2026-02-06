# Task 2.3: Error Handling and Retries (10 points)
# Create robust API functions with error handling:

import time
import random
import requests

def delay_fn(backoff_factor, max_retries, base_delay, jitter=False):
    delay_times = []
    for retry in range(max_retries):
        delay_time = base_delay * (backoff_factor ** retry)

        if jitter:
            delay_time *= random.uniform(1, 1.5)
        delay_times.append(delay_time)
    return delay_times


def make_request_with_retry(url, max_retries=3, delay=1):
    """
    Make a GET request with retry logic
    Retry on network errors and 5xx status codes
    Wait 'delay' seconds between retries
    Return: response object or None if all retries fail
    Print retry attempts
    """
    backoff = delay_fn(2,max_retries, delay, True)
    for wait_time in backoff:
        try:
            r = requests.get(url, timeout=5)
            status = r.status_code
            if 500 <= status < 600:
                print(f'Received status: {status}. Retrying in {wait_time} seconds.')
                time.sleep(wait_time)
                continue
            r.raise_for_status()
            return r
        except requests.RequestException as e:
            print(f"Network error: {e}. Retrying in {wait_time} seconds.")
            time.sleep(wait_time)
    return None

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

from functools import wraps
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
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (requests.exceptions.RequestException, ValueError, KeyError) as e:
            print(f"API call failed: {e}")
            return None
    return wrapper