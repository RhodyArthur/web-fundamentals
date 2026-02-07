# Task 3.2: Data Transformation (5 points)
# Create functions to transform API data:

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
    return {
        'id': post.get('id'),
        'title': post.get('title'),
        'preview': (post.get('body', '')[:50] + '...') if post.get('body') else '',
        'author_id': post.get('userId')
    }

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