# Task 2.1: JSONPlaceholder API Client (10 points)
# Create a client for the JSONPlaceholder API (https://jsonplaceholder.typicode.com):
import requests
from requests.exceptions import HTTPError

class JSONPlaceholderClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"
    
    def __init__(self):
        pass
    
    def get_all_posts(self):
        """
        Fetch all posts
        Return: list of post dictionaries
        """
        try:
            response = requests.get(JSONPlaceholderClient.BASE_URL)
            response.raise_for_status()
        except HTTPError as err:
            print(err)
        else:
            return response.json()

    
    def get_post(self, post_id):
        """
        Fetch a specific post by ID
        Return: post dictionary or None if not found
        Handle 404 gracefully
        """
        url = JSONPlaceholderClient.BASE_URL/post_id
        try:
            response = requests.get(url)
            response.raise_for_status()
        except HTTPError as err:
            print(err)
            return None
        else:
            return response.json()
    
    def create_post(self, title, body, user_id):
        """
        Create a new post
        Return: created post dictionary with id
        """
        pass
    
    def update_post(self, post_id, title=None, body=None):
        """
        Update a post (PUT request)
        Only update fields that are provided
        Return: updated post dictionary
        """
        pass
    
    def delete_post(self, post_id):
        """
        Delete a post
        Return: True if successful, False otherwise
        """
        pass
    
    def get_user_posts(self, user_id):
        """
        Get all posts by a specific user
        Use query parameters: ?userId=<user_id>
        Return: list of post dictionaries
        """
        pass
    
    def search_posts(self, keyword):
        """
        Search for posts containing keyword in title or body
        Fetch all posts and filter locally
        Return: list of matching posts
        """
        pass