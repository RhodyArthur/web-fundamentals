# Web Fundamentals Assessment - Weeks 5-6

**Total Points: 100 (90 base + 10 bonus)**

**Time Limit: 2-3 hours**

**Instructions:**
- Complete all tasks in Python file(s)
- Use the `requests` library for API calls
- Test with real APIs (JSONPlaceholder, GitHub API, etc.)
- Handle network errors gracefully
- Follow REST API best practices

**Required Installation:**
```bash
pip install requests
```

---

## SECTION 1: HTTP Fundamentals (15 points)

### Task 1.1: Understanding HTTP Methods (5 points)
Write functions that demonstrate different HTTP methods:

```python
import requests

def demonstrate_get(url):
    """
    Make a GET request to the URL
    Print: status code, headers (Content-Type), and response body
    Return: response object
    """
    pass

def demonstrate_post(url, data):
    """
    Make a POST request with JSON data
    Print: status code and response body
    Return: response object
    """
    pass

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

# Test with JSONPlaceholder API
# GET: https://jsonplaceholder.typicode.com/posts/1
# POST: https://jsonplaceholder.typicode.com/posts
# PUT: https://jsonplaceholder.typicode.com/posts/1
# DELETE: https://jsonplaceholder.typicode.com/posts/1
```

### Task 1.2: Working with Status Codes (5 points)
Create a function that handles different status codes:

```python
def handle_response(response):
    """
    Takes a requests.Response object and handles different status codes:
    - 200-299: Return success message and data
    - 400-499: Return client error message
    - 500-599: Return server error message
    - Others: Return generic error message
    
    Returns: tuple (success: bool, message: str, data: dict or None)
    """
    pass

def check_resource_exists(url):
    """
    Check if a resource exists at the given URL
    Return: True if status is 200, False for 404, raise exception for other errors
    """
    pass
```

### Task 1.3: Working with Headers (5 points)
Create functions that work with HTTP headers:

```python
def make_request_with_headers(url, custom_headers=None):
    """
    Make a GET request with custom headers
    Include default headers: User-Agent, Accept
    Add any custom headers provided
    Print all request headers sent
    Return: response object
    """
    pass

def extract_response_headers(url):
    """
    Make a request and extract important headers:
    - Content-Type
    - Content-Length
    - Date
    - Server
    Return: dictionary of headers
    """
    pass

def make_authenticated_request(url, token):
    """
    Make a request with Bearer token authentication
    Header format: Authorization: Bearer <token>
    Return: response object
    """
    pass
```

---

## SECTION 2: Working with REST APIs (25 points)

### Task 2.1: JSONPlaceholder API Client (10 points)
Create a client for the JSONPlaceholder API (https://jsonplaceholder.typicode.com):

```python
class JSONPlaceholderClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"
    
    def __init__(self):
        pass
    
    def get_all_posts(self):
        """
        Fetch all posts
        Return: list of post dictionaries
        """
        pass
    
    def get_post(self, post_id):
        """
        Fetch a specific post by ID
        Return: post dictionary or None if not found
        Handle 404 gracefully
        """
        pass
    
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
```

### Task 2.2: Query Parameters and Filtering (5 points)
Create functions that work with query parameters:

```python
def fetch_with_pagination(base_url, page=1, limit=10):
    """
    Fetch data with pagination parameters
    URL format: base_url?_page=<page>&_limit=<limit>
    Return: list of items
    """
    pass

def fetch_filtered_data(base_url, filters):
    """
    Fetch data with multiple filter parameters
    filters is a dict like: {'userId': 1, 'completed': True}
    Build query string from filters
    Return: list of filtered items
    """
    pass

def fetch_sorted_data(base_url, sort_by, order='asc'):
    """
    Fetch data with sorting
    sort_by: field name to sort by
    order: 'asc' or 'desc'
    URL format: base_url?_sort=<field>&_order=<order>
    Return: sorted list of items
    """
    pass
```

### Task 2.3: Error Handling and Retries (10 points)
Create robust API functions with error handling:

```python
import time

def make_request_with_retry(url, max_retries=3, delay=1):
    """
    Make a GET request with retry logic
    Retry on network errors and 5xx status codes
    Wait 'delay' seconds between retries
    Return: response object or None if all retries fail
    Print retry attempts
    """
    pass

def fetch_with_timeout(url, timeout=5):
    """
    Make a request with timeout
    Handle timeout exception gracefully
    Return: (success: bool, data/error_message)
    """
    pass

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
    pass
```

---

## SECTION 3: JSON Data Handling (15 points)

### Task 3.1: JSON Parsing and Validation (5 points)
Create functions to work with JSON data:

```python
import json

def parse_json_response(response):
    """
    Safely parse JSON from a response object
    Handle json.JSONDecodeError
    Return: (success: bool, data/error_message)
    """
    pass

def validate_post_data(data):
    """
    Validate that data contains required fields for a post:
    - title (string, non-empty)
    - body (string, non-empty)
    - userId (integer, positive)
    Return: (valid: bool, error_message or None)
    """
    pass

def extract_fields(data, fields):
    """
    Extract specific fields from a dictionary or list of dictionaries
    fields: list of field names to extract
    Example: extract_fields([{...}, {...}], ['id', 'title'])
    Return: list of dictionaries with only specified fields
    """
    pass
```

### Task 3.2: Data Transformation (5 points)
Create functions to transform API data:

```python
def transform_post(post):
    """
    Transform a post object to a simplified format:
    {
        'id': post['id'],
        'title': post['title'],
        'preview': post['body'][:50] + '...',
        'author_id': post['userId']
    }
    """
    pass

def group_posts_by_user(posts):
    """
    Group a list of posts by userId
    Return: dict where keys are userIds and values are lists of posts
    Example: {1: [post1, post2], 2: [post3], ...}
    """
    pass

def calculate_statistics(posts):
    """
    Calculate statistics from posts:
    - total_posts: total number of posts
    - avg_title_length: average title length
    - posts_per_user: dict of {userId: count}
    Return: dictionary with statistics
    """
    pass
```

### Task 3.3: Working with Nested JSON (5 points)
Create functions to handle complex JSON structures:

```python
def flatten_nested_json(data):
    """
    Flatten nested JSON structure one level
    Example: {'user': {'name': 'Alice', 'age': 25}}
    Becomes: {'user.name': 'Alice', 'user.age': 25}
    Return: flattened dictionary
    """
    pass

def extract_nested_value(data, path):
    """
    Extract value from nested JSON using dot notation
    path examples: 'user.name', 'address.city', 'items.0.name'
    Return: extracted value or None if path doesn't exist
    """
    pass
```

---

## SECTION 4: Building a Complete API Client (20 points)

### Task 4.1: GitHub API Client (20 points)
Create a comprehensive GitHub API client:

```python
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

# Test your implementation
if __name__ == "__main__":
    client = GitHubClient()
    
    # Test getting user
    user = client.get_user("octocat")
    if user:
        print(f"User: {user['login']}, Repos: {user['public_repos']}")
    
    # Test getting repositories
    repos = client.get_user_repos("octocat")
    print(f"Found {len(repos)} repositories")
    
    # Test search
    results = client.search_repositories("fastapi", language="python", max_results=5)
    for repo in results:
        print(f"- {repo['full_name']} ({repo['stargazers_count']} stars)")
    
    # Test rate limit
    rate_limit = client.get_rate_limit()
    print(f"Rate limit: {rate_limit['rate']['remaining']}/{rate_limit['rate']['limit']}")
```

---

## SECTION 5: REST API Design Principles (15 points)

### Task 5.1: Design a Blog API (8 points)
Design a RESTful API for a blog system on paper (no coding, just documentation):

Create a markdown document (`blog_api_design.md`) that includes:

1. **Resources and Endpoints**
   - List all resources (users, posts, comments, categories)
   - Define all endpoints with HTTP methods
   - Example: `GET /api/v1/posts` - Get all posts

2. **Request/Response Formats**
   - Define JSON structure for each resource
   - Include example requests and responses
   - Show query parameters for filtering/pagination

3. **Status Codes**
   - Document which status codes each endpoint returns
   - Explain when each code is used

4. **Error Responses**
   - Define standard error response format
   - Give examples of error messages

**Example format:**
```markdown
## Posts Resource

### Get All Posts
- **Endpoint:** `GET /api/v1/posts`
- **Query Parameters:**
  - `page` (integer): Page number (default: 1)
  - `limit` (integer): Items per page (default: 10)
  - `category` (string): Filter by category
  - `author_id` (integer): Filter by author
- **Response:** 200 OK
```json
{
  "data": [
    {
      "id": 1,
      "title": "My First Post",
      "body": "Content here...",
      "author_id": 1,
      "category": "tech",
      "created_at": "2024-01-15T10:30:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 10,
    "total": 45,
    "pages": 5
  }
}
```
- **Error Responses:**
  - 400: Invalid query parameters
  - 500: Server error
```

### Task 5.2: API Versioning and Best Practices (4 points)
Answer these questions in a text file (`api_best_practices.txt`):

1. **URL Naming Conventions**
   - Should URLs use plural or singular nouns? Why?
   - Should URLs have trailing slashes?
   - Give examples of good vs bad URL design

2. **API Versioning**
   - What are three ways to version an API?
   - Which method do you think is best? Why?
   - Give examples of each versioning method

3. **Pagination**
   - Why is pagination important?
   - What are two common pagination approaches?
   - Give example query parameters for each

4. **Authentication**
   - What's the difference between API Key and Bearer Token authentication?
   - Where should authentication credentials be placed (header/query/body)?
   - Why?

### Task 5.3: Understanding REST Constraints (3 points)
Write short explanations (2-3 sentences each) for these REST principles:

1. **Statelessness** - What does it mean and why is it important?
2. **Client-Server Separation** - How does this benefit API design?
3. **Resource-Based URLs** - Why use nouns instead of verbs in URLs?
4. **Standard HTTP Methods** - Why is it important to use GET, POST, PUT, DELETE correctly?

---