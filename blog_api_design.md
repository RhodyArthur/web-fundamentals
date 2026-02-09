### Task 5.1: Design a Blog API (8 points)

Design a RESTful API for a blog system on paper (no coding, just documentation):

1. **Resources and Endpoints**
   - List all resources (users, posts, comments, categories)
   - users
   - posts
   - comments
   - categories

   - Define all endpoints with HTTP methods
   - `GET /api/v1/posts` - Get all posts
   - `POST /api/v1/posts` - Create a new post
   - `GET /api/v1/posts/{postId}` - Get a single post
   - `PUT /api/v1/posts/{postId}` - Update an existing post
   - `DELETE /api/v1/posts/{postId}` - Delete a post

   - `GET /api/v1/users` - Get all users
   - `POST /api/v1/users` - Create a new user
   - `GET /api/v1/users/{userId}` - Get a single user
   - `PUT /api/v1/users/{userId}` - Update an existing user
   - `DELETE /api/v1/users/{userId}` - Delete a user

   - `GET /api/v1/comments` - Get all comments
   - `POST /api/v1/comments` - Create a new comment
   - `GET /api/v1/comments/{commentId}` - Get a single comment
   - `PUT /api/v1/comments/{commentId}` - Update a comment
   - `DELETE /api/v1/comments/{commentId}` - Delete a comment

   - `GET /api/v1/categories` - Get all categories
   - `POST /api/v1/categories` - Create a new category
   - `GET /api/v1/categories/{categoryId}` - Get a single category
   - `PUT /api/v1/categories/{categoryId}` - Update a category
   - `DELETE /api/v1/categories/{categoryId}` - Delete a category

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

````markdown
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
````

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
```
