### Frontend build stage
FROM node:20-alpine AS frontend-builder
WORKDIR /app/frontend

# Install dependencies
COPY frontend/package*.json ./
RUN npm ci

# Build static assets
COPY frontend/ .
RUN npm run build

### Backend runtime stage
FROM python:3.11-slim AS backend
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1
WORKDIR /app/backend

# Install system deps (if sqlite dev headers are needed in future they can be added here)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

# Install Python deps
COPY backend/requieriments.txt .
RUN pip install -r requieriments.txt

# Copy backend source
COPY backend/ .

# Copy built frontend into FastAPI static directory
RUN mkdir -p static
COPY --from=frontend-builder /app/frontend/dist ./static

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
