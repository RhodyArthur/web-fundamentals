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
            self.headers['Authorization'] = f"Bearer {token}"
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
        except (requests.RequestException, ValueError) as e:
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
        accepted_sort_options = ["stars", "forks", "updated"]

        try:
            if sort not in accepted_sort_options:
                raise ValueError("valid sort options are 'stars', 'forks', and 'updated'")
            if language:
                query = f"{query} language:{language}"
            r = self.session.get(url, params={"q": query, "sort": sort, "per_page":max_results})
            if r.status_code == 404:
                return None
            r.raise_for_status()
            return r.json().get('items',[])
        except (requests.RequestException, ValueError) as e:
            print(f"Error searching repository: {e}")
            return None
    
    def get_repo_languages(self, owner, repo_name):
        """
        Get programming languages used in a repository
        Endpoint: GET /repos/{owner}/{repo}/languages
        Return: dictionary of {language: bytes_of_code}
        """
        url = f"{self.BASE_URL}/repos/{owner}/{repo_name}/languages"
        try:
            response = self.session.get(url)
            if response.status_code == 404:
                return None
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching languages in a repo: {e}")
            return None
    
    def get_rate_limit(self) -> dict | None:
        """
        Check API rate limit status
        Endpoint: GET /rate_limit
        Return: dictionary with limit, remaining, and reset time
        """
        url = f"{self.BASE_URL}/rate_limit"
        try:
            response = self.session.get(url)
            if response.status_code == 404:
                return None
            response.raise_for_status()
            data = response.json()
            core = data.get("resources", {}).get("core", {})
            return {
                "limit": core.get("limit"),
                "remaining": core.get("remaining"),
                "reset": core.get("reset")
            }
        except requests.RequestException as e:
            print(f"Error fetching rate information: {e}")
            return None
            print(f"Error fetching rate information: {e}")
            return None
    
    def get_trending_repos(self, language=None, since='daily') -> list | None:
        """
        Get trending repositories
        Note: GitHub doesn't have official trending API
        Use search with created date filter
        since options: 'daily', 'weekly', 'monthly'
        Return: list of trending repositories
        """
        url = f"{self.BASE_URL}/search/repositories"
        options = ['daily', 'weekly', 'monthly']
        try:
            if since not in options:
                raise ValueError("Valid since parameters are: daily, weekly, monthly")
            from datetime import datetime, timedelta
            days = {'daily': 1, 'weekly': 7, 'monthly': 30}[since]
            date_str = (datetime.utcnow() - timedelta(days=days)).strftime('%Y-%m-%d')
            q = f"created:>{date_str}"
            if language:
                q += f" language:{language}"
            response = self.session.get(url, params={"q": q, "sort": "stars", "order": "desc"})
            if response.status_code == 404:
                return None
            response.raise_for_status()
            return response.json().get("items", [])
        except (requests.RequestException, ValueError) as e:
            print(f"Error fetching trending repositories: {e}")
            return None