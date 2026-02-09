# Building a Complete API Client (20 points)

# Task 4.1: GitHub API Client (20 points)
# Create a comprehensive GitHub API client:

import requests
class GitHubClient:
    """
    GitHub API Client (v3)
    Base URL: https://api.github.com
    Documentation: https://docs.github.com/en/rest
    """
    BASE_URL = "https://api.github.com"
    
    def __init__(self, token=None):
        """
        Initialize client with optional authentication token
        Set up session with default headers
        """
        self.token = token
        self.session = requests.Session()
        # Set up headers including User-Agent (required by GitHub)
        self.headers = {'User-Agent': 'GitHubClient/1.0'}
        if token:
            self.headers['Authorization'] = f"token {token}"
        self.session.headers.update(self.headers)
    
    def get_user(self, username):
        """
        Get user information
        Endpoint: GET /users/{username}
        Return: user dictionary or None if not found
        Handle 404 gracefully
        """
        url = f"{self.BASE_URL}/users/{username}"
        try:
            response = self.session.get(url)
            if response.status_code == 404:
                return None
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching user: {e}")
            return None
    
    def get_user_repos(self, username, sort='updated'):
        """
        Get all public repositories for a user
        Endpoint: GET /users/{username}/repos
        sort options: 'created', 'updated', 'pushed', 'full_name'
        Return: list of repository dictionaries
        """
        url = f"{self.BASE_URL}/users/{username}/repos"
        sort_options = ['created', 'updated', 'pushed', 'full_name']

        try:
            if sort not in sort_options:
                raise ValueError("Unexpected sort value")
            response = self.session.get(url, params={"sort": sort})
            if response.status_code == 404:
                return None
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching user repos: {e}")
            return None
    
    def get_repo(self, owner, repo_name):
        """
        Get repository information
        Endpoint: GET /repos/{owner}/{repo}
        Return: repository dictionary or None if not found
        """
        url = f"{self.BASE_URL}/repos/{owner}/{repo_name}"
        try:
            response = self.session.get(url)
            if response.status_code == 404:
                return None
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching repository information: {e}")
            return None
    
    def search_repositories(self, query, language=None, sort='stars', max_results=10):
        """
        Search repositories
        Endpoint: GET /search/repositories
        Parameters:
        - q: query string (add language:python if language specified)
        - sort: 'stars', 'forks', 'updated'
        - per_page: max_results
        Return: list of repository dictionaries
        """
        url = f"{self.BASE_URL}/search/repositories"
        accepted_sort_options = ["stars", "forks", " updated"]

        try:
            if sort not in accepted_sort_options:
                raise ValueError("valid sort options are 'stars', 'forks', and 'updated'")
            r = self.session.get(url, params={"q": query, "sort": sort, "per_page":max_results})
            if r.status_code == 404:
                return None
            r.raise_for_status()
            return r.json()
        except requests.RequestException as e:
            print(f"Error searching repository: {e}")
            return None
    
    def get_repo_languages(self, owner, repo_name):
        """
        Get programming languages used in a repository
        Endpoint: GET /repos/{owner}/{repo}/languages
        Return: dictionary of {language: bytes_of_code}
        """
        pass
    
    def get_rate_limit(self):
        """
        Check API rate limit status
        Endpoint: GET /rate_limit
        Return: dictionary with limit, remaining, and reset time
        """
        pass
    
    def get_trending_repos(self, language=None, since='daily'):
        """
        Get trending repositories
        Note: GitHub doesn't have official trending API
        Use search with created date filter
        since options: 'daily', 'weekly', 'monthly'
        Return: list of trending repositories
        """
        pass