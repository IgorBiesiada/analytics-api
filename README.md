# Analytics API — FastAPI, SQLModel, TimescaleDB, Docker  

## Project Overview  

**Analytics API** is a backend microservice designed to collect, store, and analyze time-series data for web applications.  
Built with **FastAPI** and **SQLModel**, the API provides endpoints for event ingestion and will allow metrics aggregation and reporting.  
The backend uses **TimescaleDB** on top of PostgreSQL for efficient time-series data storage and is fully containerized with **Docker**.  

---

## Tech Stack  

- **Python** — Backend language  
- **FastAPI** — High-performance API framework  
- **SQLModel + SQLAlchemy** — ORM and query layer  
- **TimescaleDB** — Time-series optimized PostgreSQL  
- **Docker & Docker Compose** — Containerized deployment  

---

## Current Features  

- ✅ FastAPI project with modular architecture  
- ✅ PostgreSQL + TimescaleDB integration  
- ✅ Docker & Docker Compose setup (FastAPI + TimescaleDB)

## Getting Started  

1️⃣ Clone the repository  
```bash
git clone https://github.com/IgorBiesiada/analytics-api.git  
cd analytics-api  
```

2️⃣ Run Docker Compose (FastAPI + TimescaleDB)
```bash
docker-compose up --build --watch
```

3️⃣ Access the API (FastAPI) at:
```bash
http://0.0.0.0:8002/docs 
```

4️⃣ To stop and remove running containers:
```bash
docker compose down 
```