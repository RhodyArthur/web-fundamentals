# Web Fundamentals Project

## Overview

This project demonstrates core web data engineering concepts using Python. It covers HTTP fundamentals, REST API interaction, error handling, JSON parsing/validation, data transformation, and working with real-world APIs (e.g., GitHub, JSONPlaceholder).

## Features

- HTTP requests and query parameters
- Robust error handling and retry logic
- JSON parsing and schema validation
- Data transformation and grouping
- Working with nested JSON
- REST API client for JSONPlaceholder
- GitHub API client for user, repo, and trending data

## Project Structure

```
data_transformation.py           # Data transformation and statistics
error_handling_and_retries.py    # Error handling, retry, and safe API call decorators
github_api_client.py             # GitHub API client class
http_fundamentals.py             # HTTP basics and requests
json_parsing_and_validation.py   # JSON parsing, validation, and field extraction
main.py                          # Example usage and entry point
query_parameters_and_filtering.py# Query params, filtering, sorting
README.md                        # Project documentation
web_fundamentals_assessment.md   # Assessment and instructions
working_with_nested_json.py      # Flattening and extracting from nested JSON
working_with_REST_APIs.py        # JSONPlaceholder REST API client
```

## Setup

1. **Clone the repository:**
   ```sh
   git clone <repo-url>
   cd web-fundamentals
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
   _(If requirements.txt is missing, install: requests)_

## Usage

- Run `main.py` to see example usage of the various modules.
- Each module can be imported and used independently for its specific functionality.

## Example

```python
from github_api_client import GitHubClient
client = GitHubClient()
user = client.get_user('octocat')
print(user)
```

## Testing

- You can test individual modules by running them directly or using the provided examples in `main.py`.

## License

This project is for educational purposes.
