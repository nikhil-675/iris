# ---------- Stage 1: Build ----------
    FROM python:3.9-alpine AS builder

    # Install build dependencies
    RUN apk add --no-cache build-base
    
    # Create working directory
    WORKDIR /app
    
    # Copy files
    COPY requirements.txt .
    RUN pip install --upgrade pip && pip wheel --no-cache-dir --wheel-dir /wheels -r requirements.txt
    
    # ---------- Stage 2: Final ----------
    FROM python:3.9-alpine
    
    # Install runtime dependencies
    RUN apk add --no-cache libstdc++ && pip install --no-cache --no-index --find-links=/wheels -r /wheels/requirements.txt
    
    WORKDIR /app
    
    # Copy app
    COPY --from=builder /wheels /wheels
    COPY src/ ./src/
    COPY .env .
    COPY src/utils/iris_pipeline.pkl ./src/utils/iris_pipeline.pkl
    
    # Expose Flask port
    EXPOSE 5000
    
    # Run app
    CMD ["python", "-m", "src.main.app"]
    