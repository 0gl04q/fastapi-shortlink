# ShortLink

![изображение](https://github.com/user-attachments/assets/39a44ab7-f9c7-4faf-a287-46da6aab7424)

This project is a simple URL shortener built using FastAPI. It allows users to generate short links that redirect to the original URL.

## Features
- Generate short links from long URLs
- Redirect to the original URL when the short link is accessed
- API endpoints for creating and retrieving short links

## Installation
Clone the repository:
```bash
git clone https://github.com/0gl04q/fastapi-shortlink.git
```

Build and run Dockerfile:
```bash
docker build --tag shortlink .
docker run -d --name shortlink_container shortlink
```

## API Endpoints
POST /generate - Generate a short link.
- Request body: `url: https://www.example.com`
- Response: `http://example:8000/abc123`
