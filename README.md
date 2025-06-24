<div id="top">

<!-- HEADER STYLE: CLASSIC -->
<div align="center">

# <code>❯ Data PANP - FastAPI Blog</code>

<em></em>

<!-- BADGES  -->
<!-- local repository, no metadata badges. -->

<em>Built with the tools and technologies:</em>

<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=default&logo=JavaScript&logoColor=black" alt="JavaScript">
<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=default&logo=FastAPI&logoColor=white" alt="FastAPI">
<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=default&logo=Pytest&logoColor=white" alt="Pytest">
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=default&logo=Docker&logoColor=white" alt="Docker">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=default&logo=Python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/Pydantic-E92063.svg?style=default&logo=Pydantic&logoColor=white" alt="Pydantic">

</div>
<br>

**Version:** 1.0.0  
**Summary:** A REST API for delivering blog posts to Data Panp's platform..

---

## Overview

This is a FastAPI-based REST API that serves blog content for the Data Panp platform.  
The API is built with clean architecture, modular design, and production-ready standards, including exception handling, linting, and pre-commit hooks.

---

## Project Structure

```sh
└── /
    ├── Dockerfile
    ├── Justfile
    ├── README.md
    ├── __pycache__
    │   └── app.cpython-313.pyc
    ├── app
    │   ├── __pycache__
    │   ├── core
    │   ├── data_doc.py
    │   ├── exceptions.py
    │   ├── main.py
    │   ├── models.py
    │   ├── routes
    │   └── utils.py
    ├── dev-requirements.in
    ├── dev-requirements.txt
    ├── docker-compose.yml
    ├── mongo-init
    │   └── init.js
    ├── requirements.in
    ├── requirements.txt
    └── test_api.py
```

---

## API Base Path

All endpoints are versioned under `/api/v1`.

---

## Running the Application

You can run the application in two ways:

---

### Option 1️⃣ — Docker Compose (Recommended)

> No manual setup required — everything will be built and started automatically.

```bash
docker-compose up --build
```

---

## Option 2️⃣ — Manual Development Setup (Local Virtual Environment)

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

---

## Contributing

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your LOCAL account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone .
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to LOCAL**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

---

## Author

[Robson Araujo Carmo](https://github.com/RobsonAraujo)
