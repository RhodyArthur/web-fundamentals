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
        url = f'{JSONPlaceholderClient.BASE_URL}/posts'
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except HTTPError as err:
            print(f"HTTP error occurred: {err}")
        except Exception as err:
            print(f"Other error occurred: {err}")
        return []

    
    def get_post(self, post_id):
        """
        Fetch a specific post by ID
        Return: post dictionary or None if not found
        Handle 404 gracefully
        """
        url = f'{JSONPlaceholderClient.BASE_URL}/posts/{post_id}'
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except HTTPError as err:
            print(f"HTTP error occurred: {err}")
        except Exception as err:
            print(f"Other error occurred: {err}")
        return None
    
    def create_post(self, title, body, user_id):
        """
        Create a new post
        Return: created post dictionary with id
        """
        url = f'{JSONPlaceholderClient.BASE_URL}/posts'
        data = {
            "userId": user_id,
            "title": title,
            "body": body
        }
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()
        except HTTPError as err:
            print(err)
        else:
            return response.json()
    
    def update_post(self, post_id, title=None, body=None):
        """
        Update a post (PUT request)
        Only update fields that are provided
        Return: updated post dictionary
        """
        url = JSONPlaceholderClient.BASE_URL/post_id
        all_data = self.get_all_posts()
        if all_data["id"] == post_id:
            all_data["title"] = title
            all_data["body"] = body

        try:
            response = requests.put(url, all_data["id"])
            response.raise_for_status()
        except HTTPError as err:
            print(err)
            return None
        else:
            return response.json()
    
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