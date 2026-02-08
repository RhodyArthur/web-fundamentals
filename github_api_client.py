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
        pass
    
    def get_user(self, username):
        """
        Get user information
        Endpoint: GET /users/{username}
        Return: user dictionary or None if not found
        Handle 404 gracefully
        """
        pass
    
    def get_user_repos(self, username, sort='updated'):
        """
        Get all public repositories for a user
        Endpoint: GET /users/{username}/repos
        sort options: 'created', 'updated', 'pushed', 'full_name'
        Return: list of repository dictionaries
        """
        pass
    
    def get_repo(self, owner, repo_name):
        """
        Get repository information
        Endpoint: GET /repos/{owner}/{repo}
        Return: repository dictionary or None if not found
        """
        pass
    
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
        pass
    
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