# ─────────────────────────────────────────────
# Stage 1: Vite + React 프론트엔드 빌드
# ─────────────────────────────────────────────
FROM node:20-alpine AS builder

WORKDIR /app

# 패키지 의존성 파일 복사 및 설치
COPY package*.json ./
RUN npm ci

# 소스 복사 및 빌드
COPY . .
RUN npm run build

# ─────────────────────────────────────────────
# Stage 2: Python + FastAPI 백엔드 런타임
# ─────────────────────────────────────────────
FROM python:3.11-slim

WORKDIR /app

# C 컴파일러 및 필수 라이브러리 설치 (pyproj, lxml 빌드용)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 파이썬 의존성 설치
COPY server/requirements.txt ./server/requirements.txt
RUN pip install --no-cache-dir -r server/requirements.txt

# 서버 소스코드 복사
COPY server/ ./server/

# Stage 1에서 빌드된 정적 리소스를 서버의 dist 폴더로 복사
COPY --from=builder /app/dist ./dist/

# 포트 노출
EXPOSE 8005

# 백엔드 서버 구동
CMD ["python", "server/main.py"]
