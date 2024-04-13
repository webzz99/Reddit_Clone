# Reddit C

This is a social media project

### About Author

- **Author Name**: Ali
- **Email**: avolkan99@gmail.com

### Reddit C

- This is a social media project that allow users to post the feed and other users are able to vote the feed. {CONTINUE}

### Error handling

- There are two custom exception: ResponseFailureException and AuthorizationException.
- There is a decorator [Link Text](/server/util/response_builder.py) response builder which will take care of the shape of the response for both success and failed responses.

## Prerequisites

- Python 3.10 installed on your system

## Installation


```bash
cd redditC
```

## Setup

### 1. Create a Virtual Environment (Optional but Recommended)

Create a virtual environment to manage project dependencies:

```bash
python -m venv venv
```

### Activate the virtual environment:

#### On macOS and Linux:

```bash
source venv/bin/activate
```

#### On Windows:

```bash
venv\Scripts\activate.bat
```

## Run server locally

```bash
chmod +x start_server.sh
./run_server.sh
```

## OR Run server with Docker (recommended)

```bash
docker build -t redditC .
docker run -p 8080:8080 redditC
```

## Server and its APIs

The localhost server will be running on http://localhost:8080 at port 8080

It has two apis for version1 and version2 respectively.

#### User API

```
http://localhost:8080/api/v1/users
```

#### POST API

```
http://localhost:8080/api/v2/posts
```
