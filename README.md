# Data Panp - Blog API

**Version:** 1.0.0  
**Summary:** A REST API for delivering blog posts to Data Panp's platform.

---

## Overview

This is a FastAPI-based REST API that serves blog content for the Data Panp platform.  
The API is built with clean architecture, modular design, and production-ready standards, including exception handling, linting, and pre-commit hooks.

---

## Tech Stack

- **Python 3.11+**
- **FastAPI**
- **MongoDB (NoSQL database)**
- **Pydantic models**
- **Ruff (Linter)**
- **Black (Formatter)**
- **Pre-commit hooks**

---

## API Base Path

All endpoints are versioned under `/api/v1`.

---

## Development Setup

### 1️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the application

```bash
uvicorn app.main:app --reload
```

## Author

[Robson Araujo Carmo](https://github.com/RobsonAraujo)
