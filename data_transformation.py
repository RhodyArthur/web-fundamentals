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
    body = post.get('body')
    return {
        'id': post.get('id'),
        'title': post.get('title'),
        'preview': body[:50] + ('...' if len(body) > 50 else ''),
        'author_id': post.get('userId')
    }

def group_posts_by_user(posts: list[dict]) -> dict:
    """
    Group a list of posts by userId
    Return: dict where keys are userIds and values are lists of posts
    Example: {1: [post1, post2], 2: [post3], ...}
    """
    grouped = {}
    if posts is None:
        return {}
    for post in posts:
        userId = post.get('userId')
        if userId in grouped:
            grouped[userId].append(post)
        else:
            grouped[userId] = [post]
    return grouped

def calculate_statistics(posts) -> dict:
    """
    Calculate statistics from posts:
    - total_posts: total number of posts
    - avg_title_length: average title length
    - posts_per_user: dict of {userId: count}
    Return: dictionary with statistics
    """
    if posts is None:
        return {}
    total_posts = len(posts)

    title_lengths = []
    posts_per_user = {}
    for post in posts:
        title_length = len(post.get('title',''))
        userId = post.get('userId')
        title_lengths.append(title_length)

        if userId in posts_per_user:
            posts_per_user[userId] += 1
        else:
            posts_per_user[userId] = 1
    avg_title_length = sum(title_lengths) / total_posts if total_posts > 0 else 0

    return {
  "total_posts": total_posts,
  "avg_title_length": avg_title_length,
  "posts_per_user": posts_per_user
}


