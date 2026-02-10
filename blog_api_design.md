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

## Posts Resource

### Get All Posts

- **Endpoint:** `GET /api/v1/posts`
- **Query Parameters:**
  - `page` (integer): Page number (default: 1)
  - `limit` (integer): Items per page (default: 10)
  - `category` (string): Filter by category
  - `author_id` (integer): Filter by author
  - `status` (string): Filter by status (draft, published, archived)
- **Success Response:** 200 OK

```json
{
  "data": [
    {
      "id": 1,
      "title": "My First Post",
      "body": "Content here...",
      "author_id": 1,
      "category_id": 3,
      "status": "published",
      "created_at": "2024-01-15T10:30:00Z",
      "updated_at": "2024-01-15T10:30:00Z"
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
  - 400 Bad Request: Invalid query parameters
  - 500 Internal Server Error: Server error

### Get Single Post

- **Endpoint:** `GET /api/v1/posts/{postId}`
- **Success Response:** 200 OK

```json
{
  "id": 1,
  "title": "My First Post",
  "body": "Content here...",
  "author_id": 1,
  "category_id": 3,
  "status": "published",
  "created_at": "2024-01-15T10:30:00Z",
  "updated_at": "2024-01-15T10:30:00Z"
}
```

- **Error Responses:**
  - 404 Not Found: Post not found
  - 500 Internal Server Error: Server error

### Create Post

- **Endpoint:** `POST /api/v1/posts`
- **Request Body:**

```json
{
  "title": "New Post Title",
  "body": "Post content here...",
  "author_id": 1,
  "category_id": 3,
  "status": "published"
}
```

- **Success Response:** 201 Created

```json
{
  "id": 2,
  "title": "New Post Title",
  "body": "Post content here...",
  "author_id": 1,
  "category_id": 3,
  "status": "published",
  "created_at": "2024-01-16T10:30:00Z",
  "updated_at": "2024-01-16T10:30:00Z"
}
```

- **Error Responses:**
  - 400 Bad Request: Invalid input data
  - 401 Unauthorized: Authentication required
  - 422 Unprocessable Entity: Validation errors
  - 500 Internal Server Error: Server error

### Update Post

- **Endpoint:** `PUT /api/v1/posts/{postId}`
- **Request Body:**

```json
{
  "title": "Updated Post Title",
  "body": "Updated content here...",
  "category_id": 4,
  "status": "published"
}
```

- **Success Response:** 200 OK

```json
{
  "id": 1,
  "title": "Updated Post Title",
  "body": "Updated content here...",
  "author_id": 1,
  "category_id": 4,
  "status": "published",
  "created_at": "2024-01-15T10:30:00Z",
  "updated_at": "2024-01-16T11:00:00Z"
}
```

- **Error Responses:**
  - 400 Bad Request: Invalid input data
  - 401 Unauthorized: Authentication required
  - 404 Not Found: Post not found
  - 422 Unprocessable Entity: Validation errors
  - 500 Internal Server Error: Server error

### Delete Post

- **Endpoint:** `DELETE /api/v1/posts/{postId}`
- **Success Response:** 204 No Content

- **Error Responses:**
  - 401 Unauthorized: Authentication required
  - 404 Not Found: Post not found
  - 500 Internal Server Error: Server error

---

## Users Resource

### Get All Users

- **Endpoint:** `GET /api/v1/users`
- **Query Parameters:**
  - `page` (integer): Page number (default: 1)
  - `limit` (integer): Items per page (default: 10)
  - `role` (string): Filter by role (admin, author, reader)
- **Success Response:** 200 OK

```json
{
  "data": [
    {
      "id": 1,
      "username": "johndoe",
      "email": "john@example.com",
      "role": "author",
      "created_at": "2024-01-10T08:00:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 10,
    "total": 25,
    "pages": 3
  }
}
```

- **Error Responses:**
  - 400 Bad Request: Invalid query parameters
  - 401 Unauthorized: Authentication required
  - 500 Internal Server Error: Server error

### Get Single User

- **Endpoint:** `GET /api/v1/users/{userId}`
- **Success Response:** 200 OK

```json
{
  "id": 1,
  "username": "johndoe",
  "email": "john@example.com",
  "role": "author",
  "bio": "Tech enthusiast and blogger",
  "created_at": "2024-01-10T08:00:00Z",
  "updated_at": "2024-01-10T08:00:00Z"
}
```

- **Error Responses:**
  - 404 Not Found: User not found
  - 500 Internal Server Error: Server error

### Create User

- **Endpoint:** `POST /api/v1/users`
- **Request Body:**

```json
{
  "username": "janedoe",
  "email": "jane@example.com",
  "password": "securepassword123",
  "role": "author",
  "bio": "Writer and photographer"
}
```

- **Success Response:** 201 Created

```json
{
  "id": 2,
  "username": "janedoe",
  "email": "jane@example.com",
  "role": "author",
  "bio": "Writer and photographer",
  "created_at": "2024-01-16T09:00:00Z",
  "updated_at": "2024-01-16T09:00:00Z"
}
```

- **Error Responses:**
  - 400 Bad Request: Invalid input data
  - 409 Conflict: Username or email already exists
  - 422 Unprocessable Entity: Validation errors
  - 500 Internal Server Error: Server error

### Update User

- **Endpoint:** `PUT /api/v1/users/{userId}`
- **Request Body:**

```json
{
  "email": "newemail@example.com",
  "bio": "Updated bio",
  "role": "admin"
}
```

- **Success Response:** 200 OK

```json
{
  "id": 1,
  "username": "johndoe",
  "email": "newemail@example.com",
  "role": "admin",
  "bio": "Updated bio",
  "created_at": "2024-01-10T08:00:00Z",
  "updated_at": "2024-01-16T10:00:00Z"
}
```

- **Error Responses:**
  - 400 Bad Request: Invalid input data
  - 401 Unauthorized: Authentication required
  - 403 Forbidden: Insufficient permissions
  - 404 Not Found: User not found
  - 422 Unprocessable Entity: Validation errors
  - 500 Internal Server Error: Server error

### Delete User

- **Endpoint:** `DELETE /api/v1/users/{userId}`
- **Success Response:** 204 No Content

- **Error Responses:**
  - 401 Unauthorized: Authentication required
  - 403 Forbidden: Insufficient permissions
  - 404 Not Found: User not found
  - 500 Internal Server Error: Server error

---

## Comments Resource

### Get All Comments

- **Endpoint:** `GET /api/v1/comments`
- **Query Parameters:**
  - `page` (integer): Page number (default: 1)
  - `limit` (integer): Items per page (default: 10)
  - `post_id` (integer): Filter by post
  - `user_id` (integer): Filter by user
- **Success Response:** 200 OK

```json
{
  "data": [
    {
      "id": 1,
      "post_id": 1,
      "user_id": 2,
      "body": "Great post!",
      "created_at": "2024-01-15T12:00:00Z",
      "updated_at": "2024-01-15T12:00:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 10,
    "total": 150,
    "pages": 15
  }
}
```

- **Error Responses:**
  - 400 Bad Request: Invalid query parameters
  - 500 Internal Server Error: Server error

### Get Single Comment

- **Endpoint:** `GET /api/v1/comments/{commentId}`
- **Success Response:** 200 OK

```json
{
  "id": 1,
  "post_id": 1,
  "user_id": 2,
  "body": "Great post!",
  "created_at": "2024-01-15T12:00:00Z",
  "updated_at": "2024-01-15T12:00:00Z"
}
```

- **Error Responses:**
  - 404 Not Found: Comment not found
  - 500 Internal Server Error: Server error

### Create Comment

- **Endpoint:** `POST /api/v1/comments`
- **Request Body:**

```json
{
  "post_id": 1,
  "user_id": 2,
  "body": "This is a great article!"
}
```

- **Success Response:** 201 Created

```json
{
  "id": 2,
  "post_id": 1,
  "user_id": 2,
  "body": "This is a great article!",
  "created_at": "2024-01-16T13:00:00Z",
  "updated_at": "2024-01-16T13:00:00Z"
}
```

- **Error Responses:**
  - 400 Bad Request: Invalid input data
  - 401 Unauthorized: Authentication required
  - 404 Not Found: Post or user not found
  - 422 Unprocessable Entity: Validation errors
  - 500 Internal Server Error: Server error

### Update Comment

- **Endpoint:** `PUT /api/v1/comments/{commentId}`
- **Request Body:**

```json
{
  "body": "Updated comment text"
}
```

- **Success Response:** 200 OK

```json
{
  "id": 1,
  "post_id": 1,
  "user_id": 2,
  "body": "Updated comment text",
  "created_at": "2024-01-15T12:00:00Z",
  "updated_at": "2024-01-16T14:00:00Z"
}
```

- **Error Responses:**
  - 400 Bad Request: Invalid input data
  - 401 Unauthorized: Authentication required
  - 403 Forbidden: User can only edit their own comments
  - 404 Not Found: Comment not found
  - 422 Unprocessable Entity: Validation errors
  - 500 Internal Server Error: Server error

### Delete Comment

- **Endpoint:** `DELETE /api/v1/comments/{commentId}`
- **Success Response:** 204 No Content

- **Error Responses:**
  - 401 Unauthorized: Authentication required
  - 403 Forbidden: User can only delete their own comments
  - 404 Not Found: Comment not found
  - 500 Internal Server Error: Server error

---

## Categories Resource

### Get All Categories

- **Endpoint:** `GET /api/v1/categories`
- **Query Parameters:**
  - `page` (integer): Page number (default: 1)
  - `limit` (integer): Items per page (default: 10)
- **Success Response:** 200 OK

```json
{
  "data": [
    {
      "id": 1,
      "name": "Technology",
      "slug": "technology",
      "description": "Tech-related posts",
      "created_at": "2024-01-01T00:00:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 10,
    "total": 12,
    "pages": 2
  }
}
```

- **Error Responses:**
  - 400 Bad Request: Invalid query parameters
  - 500 Internal Server Error: Server error

### Get Single Category

- **Endpoint:** `GET /api/v1/categories/{categoryId}`
- **Success Response:** 200 OK

```json
{
  "id": 1,
  "name": "Technology",
  "slug": "technology",
  "description": "Tech-related posts",
  "created_at": "2024-01-01T00:00:00Z",
  "updated_at": "2024-01-01T00:00:00Z"
}
```

- **Error Responses:**
  - 404 Not Found: Category not found
  - 500 Internal Server Error: Server error

### Create Category

- **Endpoint:** `POST /api/v1/categories`
- **Request Body:**

```json
{
  "name": "Travel",
  "slug": "travel",
  "description": "Travel and adventure posts"
}
```

- **Success Response:** 201 Created

```json
{
  "id": 2,
  "name": "Travel",
  "slug": "travel",
  "description": "Travel and adventure posts",
  "created_at": "2024-01-16T15:00:00Z",
  "updated_at": "2024-01-16T15:00:00Z"
}
```

- **Error Responses:**
  - 400 Bad Request: Invalid input data
  - 401 Unauthorized: Authentication required
  - 403 Forbidden: Admin access required
  - 409 Conflict: Category name or slug already exists
  - 422 Unprocessable Entity: Validation errors
  - 500 Internal Server Error: Server error

### Update Category

- **Endpoint:** `PUT /api/v1/categories/{categoryId}`
- **Request Body:**

```json
{
  "name": "Technology & Science",
  "description": "Tech and science posts"
}
```

- **Success Response:** 200 OK

```json
{
  "id": 1,
  "name": "Technology & Science",
  "slug": "technology",
  "description": "Tech and science posts",
  "created_at": "2024-01-01T00:00:00Z",
  "updated_at": "2024-01-16T16:00:00Z"
}
```

- **Error Responses:**
  - 400 Bad Request: Invalid input data
  - 401 Unauthorized: Authentication required
  - 403 Forbidden: Admin access required
  - 404 Not Found: Category not found
  - 422 Unprocessable Entity: Validation errors
  - 500 Internal Server Error: Server error

### Delete Category

- **Endpoint:** `DELETE /api/v1/categories/{categoryId}`
- **Success Response:** 204 No Content

- **Error Responses:**
  - 401 Unauthorized: Authentication required
  - 403 Forbidden: Admin access required
  - 404 Not Found: Category not found
  - 409 Conflict: Category has associated posts
  - 500 Internal Server Error: Server error

---

3. **Status Codes**

The API uses standard HTTP status codes:

- **200 OK**: Request successful for GET, PUT operations
- **201 Created**: Resource successfully created (POST operations)
- **204 No Content**: Resource successfully deleted (DELETE operations)
- **400 Bad Request**: Invalid request format or parameters
- **401 Unauthorized**: Authentication credentials missing or invalid
- **403 Forbidden**: Authenticated but lacks permission for the operation
- **404 Not Found**: Requested resource doesn't exist
- **409 Conflict**: Request conflicts with existing resource (e.g., duplicate username)
- **422 Unprocessable Entity**: Request format is correct but contains validation errors
- **500 Internal Server Error**: Server encountered an unexpected error

4. **Error Responses**

Standard error response format for all endpoints:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": [
      {
        "field": "email",
        "message": "Email format is invalid"
      },
      {
        "field": "password",
        "message": "Password must be at least 8 characters"
      }
    ],
    "timestamp": "2024-01-16T10:30:00Z"
  }
}
```

**Example Error Scenarios:**

**404 Not Found:**

```json
{
  "error": {
    "code": "NOT_FOUND",
    "message": "Post with ID 999 not found",
    "timestamp": "2024-01-16T10:30:00Z"
  }
}
```

**401 Unauthorized:**

```json
{
  "error": {
    "code": "UNAUTHORIZED",
    "message": "Authentication credentials are required",
    "timestamp": "2024-01-16T10:30:00Z"
  }
}
```

**403 Forbidden:**

```json
{
  "error": {
    "code": "FORBIDDEN",
    "message": "You do not have permission to delete this comment",
    "timestamp": "2024-01-16T10:30:00Z"
  }
}
```

**409 Conflict:**

```json
{
  "error": {
    "code": "DUPLICATE_RESOURCE",
    "message": "A user with this email already exists",
    "timestamp": "2024-01-16T10:30:00Z"
  }
}
```

**500 Internal Server Error:**

```json
{
  "error": {
    "code": "INTERNAL_SERVER_ERROR",
    "message": "An unexpected error occurred. Please try again later.",
    "timestamp": "2024-01-16T10:30:00Z"
  }
}
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

Statelessness means that each API request must contain all the information needed to process it, and the server doesn't store any client context between requests. Every request is independent and self-contained, with authentication credentials and necessary data included in each call. This is important because it makes the API more scalable (servers don't need to maintain session state), more reliable (no session data to lose), and easier to load balance across multiple servers.

2. **Client-Server Separation** - How does this benefit API design?

Client-server separation means that the client (user interface) and server (data storage and business logic) are independent components that communicate only through the API interface. This allows the client and server to evolve independently—the frontend can be redesigned without changing the backend, and vice versa. This separation improves scalability, maintainability, and enables different clients (web, mobile, desktop) to use the same API.

3. **Resource-Based URLs** - Why use nouns instead of verbs in URLs?

Resource-based URLs use nouns to represent entities (like /users, /posts, /comments) rather than verbs (like /getUsers, /createPost) because the HTTP methods (GET, POST, PUT, DELETE) already specify the action being performed. This creates cleaner, more intuitive URLs that focus on "what" (the resource) rather than "how" (the action). It also makes the API more consistent and easier to understand, as resources are identified by their nature, not by operations performed on them.

4. **Standard HTTP Methods** - Why is it important to use GET, POST, PUT, DELETE correctly?

Using HTTP methods correctly ensures predictable and consistent API behavior that follows widely accepted conventions. Each method has specific semantics and expectations: GET should be safe (read-only) and idempotent, POST creates resources, PUT updates them, and DELETE removes them. This standardization enables proper caching, improves security (browsers treat GET differently from POST), and makes the API intuitive for developers who understand REST principles.

```

```
