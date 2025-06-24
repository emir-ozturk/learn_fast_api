# FastAPI Application

A clean FastAPI application with async SQLAlchemy support and PostgreSQL database.

## Features

- FastAPI with async/await support
- SQLAlchemy with async database operations
- Pydantic for data validation
- PostgreSQL database
- Clean architecture with repositories and services
- Docker support

## Quick Start with Docker

### Prerequisites

- Docker
- Docker Compose

### Run with Docker Compose

1. Clone the repository
```bash
git clone <your-repo-url>
cd learn_fast_api
```

2. Create environment file
```bash
cp .env.example .env
```

3. Start the application
```bash
docker-compose up --build
```

The application will be available at:
- API: http://localhost:8000
- Documentation: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Run with Docker only

1. Build the image
```bash
docker build -t fastapi-app .
```

2. Run PostgreSQL
```bash
docker run -d \
  --name postgres-db \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=password \
  -e POSTGRES_DB=fastapi_db \
  -p 5432:5432 \
  postgres:15-alpine
```

3. Run the application
```bash
docker run -d \
  --name fastapi-app \
  -p 8000:8000 \
  -e DATABASE_URL=postgresql+asyncpg://postgres:password@host.docker.internal:5432/fastapi_db \
  --link postgres-db \
  fastapi-app
```

## Development

### Local Development

1. Install dependencies
```bash
pip install -r requirements.txt
```

2. Set up environment variables
```bash
cp .env.example .env
# Edit .env with your database configuration
```

3. Run the application
```bash
uvicorn app.main:app --reload
```

### API Endpoints

- `POST /users/` - Create a new user
- `GET /users/` - List all users
- `GET /users/{user_id}` - Get user by ID

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection string | Required |
| `APP_NAME` | Application name | `MyFastAPI` |

## Docker Configuration

### Dockerfile Features

- Multi-stage build for optimization
- Non-root user for security
- Health check endpoint
- Proper Python environment setup
- Minimal system dependencies

### Docker Compose Features

- Application and database orchestration
- Volume persistence for PostgreSQL
- Environment variable configuration
- Development-friendly setup

## Production Deployment

For production deployment, consider:

1. Use environment-specific `.env` files
2. Set up proper database credentials
3. Configure reverse proxy (nginx)
4. Set up SSL certificates
5. Use container orchestration (Kubernetes, Docker Swarm)

## Database Migration

The application uses SQLAlchemy models. For production, you might want to add Alembic for database migrations:

```bash
pip install alembic
alembic init migrations
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
``` 