#  Task 3.1: JSON Parsing and Validation (5 points)
# Create functions to work with JSON data:

import json

def parse_json_response(response):
    """
    Safely parse JSON from a response object
    Handle json.JSONDecodeError
    Return: (success: bool, data/error_message)
    """
    try:
        result = response.json()
        return (True, result)
    except (json.JSONDecodeError, ValueError) as e:
        return (False, str(e))

def validate_post_data(data):
    """
    Validate that data contains required fields for a post:
    - title (string, non-empty)
    - body (string, non-empty)
    - userId (integer, positive)
    Return: (valid: bool, error_message or None)
    """

    if data is None:
        return (False, 'Data is required')
    
    title = data.get("title")
    if not isinstance(title, str) or not title.strip():
        return (False, 'title is required and must be a non-empty string')
    
    body = data.get("body")
    if not isinstance(body, str) or not body.strip():
        return (False, 'body is required and must be a non-empty string')
    
    userId = data.get("userId")
    if not isinstance(userId, int) or userId <= 0:
        return (False, 'userId is required and must be a positive integer')
    return (True, None)

def extract_fields(data, fields):
    """
    Extract specific fields from a dictionary or list of dictionaries
    fields: list of field names to extract
    Example: extract_fields([{...}, {...}], ['id', 'title'])
    Return: list of dictionaries with only specified fields
    """
    if isinstance(data, dict):
        data = [data]
    result = []
    for item in data:
        extracted = {field: item.get(field) for field in fields}
        result.append(extracted)
    return result