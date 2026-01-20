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
    print(f"Status Code: {r.status_code}\n Headrs (Content-Type): {r.headers["Content-Type"]} \n Response body: {r.text}")
    return r

def demonstrate_post(url, data):
    """
    Make a POST request with JSON data
    Print: status code and response body
    Return: response object
    """
    response = requests.post(url, data)
    print(f"Status code: {response.status_code}, Body: {response.text}")

def demonstrate_put(url, data):
    """
    Make a PUT request to update a resource
    Print: status code and response body
    Return: response object
    """
    pass

def demonstrate_delete(url):
    """
    Make a DELETE request
    Print: status code
    Return: True if successful (status 200-299), False otherwise
    """
    pass