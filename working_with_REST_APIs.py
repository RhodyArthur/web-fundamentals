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
            return response.json()
        except HTTPError as err:
            print(f"HTTP error occurred: {err}")
        except Exception as err:
            print(f"Other error occurred: {err}")
        return None
    
    def update_post(self, post_id, title=None, body=None):
        """
        Update a post (PUT request)
        Only update fields that are provided
        Return: updated post dictionary
        """
        url = f'{JSONPlaceholderClient.BASE_URL}/posts/{post_id}'

        data = self.get_post(post_id)

        if data is None:
            print(f"Post with id {post_id} not found.")
            return False
        
        if title is not None:
            data["title"] = title

        if body is not None:
            data["body"] = body

        try:
            response = requests.put(url, json=data)
            response.raise_for_status()
            return response.json()
        except HTTPError as err:
            print(f"HTTP error occurred: {err}")
        except Exception as err:
            print(f"Other error occurred: {err}")
        return None
    
    def delete_post(self, post_id):
        """
        Delete a post
        Return: True if successful, False otherwise
        """
        url = f'{JSONPlaceholderClient.BASE_URL}/posts/{post_id}'

        data = self.get_post(post_id)

        if data is None:
            print(f"Post with id {post_id} not found.")
            return False
        
        try:
            response = requests.delete(url)
            response.raise_for_status()
            return True
        except HTTPError as err:
            print(f"HTTP error occurred: {err}")
        except Exception as err:
            print(f"Other error occurred: {err}")
        return False
    
    def get_user_posts(self, user_id):
        """
        Get all posts by a specific user
        Use query parameters: ?userId=<user_id>
        Return: list of post dictionaries
        """
        url = f'{JSONPlaceholderClient.BASE_URL}/posts'
        try:
            response = requests.get(url, params={"userId":user_id})
            response.raise_for_status()
            return response.json()
        except HTTPError as err:
            print(f"HTTP error occurred: {err}")
        except Exception as err:
            print(f"Other error occurred: {err}")
        return []
    
    def search_posts(self, keyword):
        """
        Search for posts containing keyword in title or body
        Fetch all posts and filter locally
        Return: list of matching posts
        """
        all_posts = self.get_all_posts()
        matches = []
        for post in all_posts:
            if keyword.lower() in post["title"].lower() or keyword.lower() in post["body"].lower():
                matches.append(post)
        return matches