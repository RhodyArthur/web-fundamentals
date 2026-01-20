# Task 1.1: Understanding HTTP Methods (5 points)
# Write functions that demonstrate different HTTP methods:

import requests
BASE_URL = 'https://jsonplaceholder.typicode.com/posts'

def demonstrate_get(url):
    """
    Make a GET request to the URL
    Print: status code, headers (Content-Type), and response body
    Return: response object
    """
    r = requests.get(url, params={"q":1})
    print(f"Status Code: {r.status_code}\n Headers (Content-Type): {r.headers['Content-Type']} \n Response body: {r.text}")
    return r

def demonstrate_post(url, data):
    """
    Make a POST request with JSON data
    Print: status code and response body
    Return: response object
    """
    response = requests.post(url, json=data)
    print(f"Status code: {response.status_code}, Body: {response.text}")
    return response

def demonstrate_put(url, data):
    """
    Make a PUT request to update a resource
    Print: status code and response body
    Return: response object
    """
    response = requests.put(url, json=data)
    print(f"Status code: {response.status_code}, Body: {response.text}")
    return response


def demonstrate_delete(url):
    """
    Make a DELETE request
    Print: status code
    Return: True if successful (status 200-299), False otherwise
    """
    response = requests.delete(url)
    if response.status_code > 199 and response.status_code < 300:
        print(f"Status code: {response.status_code}")
        return True
    else:
        return False

# Task 1.2: Working with Status Codes (5 points)
# Create a function that handles different status codes:

def handle_response(response):
    """
    Takes a requests.Response object and handles different status codes:
    - 200-299: Return success message and data
    - 400-499: Return client error message
    - 500-599: Return server error message
    - Others: Return generic error message
    
    Returns: tuple (success: bool, message: str, data: dict or None)
    """
    if 200 <= response.status_code < 300:
        try:
            data = response.json()
        except ValueError:
            data = response.text
        return (True, f'Successful request ({response.status_code})', data)
    elif 400 <= response.status_code < 500:
        return (False, f"Client side error ({response.status_code})", None)
    elif 500 <= response.status_code < 600:
        return (False, f"Server side error ({response.status_code})", None)
    else:
        return (False, f"Generic error ({response.status_code})", None)

def check_resource_exists(url):
    """
    Check if a resource exists at the given URL
    Return: True if status is 200, False for 404, raise exception for other errors
    """
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return True
        elif r.status_code == 404:
            return False
        else:
            raise Exception(f"Unexpected status code: {r.status_code}")
    except Exception as err:
        print(err)
        raise