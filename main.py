
from github_api_client import GitHubClient
def main():
    pass

if __name__ == "__main__":
    client = GitHubClient()
    
    # Test getting user
    user = client.get_user("octocat")
    if user:
        print(f"User: {user['login']}, Repos: {user['public_repos']}")
    
    # Test getting repositories
    repos = client.get_user_repos("octocat")
    if repos:
        print(f"Found {len(repos)} repositories")
    
    # Test search
    results = client.search_repositories("fastapi", language="python", max_results=5)
    if results:
        for repo in results:
            print(f"- {repo['full_name']} ({repo['stargazers_count']} stars)")
    
    # Test rate limit
    rate_limit = client.get_rate_limit()
    if rate_limit:
        print(f"Rate limit: {rate_limit['remaining']}/{rate_limit['limit']}")