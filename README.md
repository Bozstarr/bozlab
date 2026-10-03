# BozLab

A backend project built with FastAPI.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run the development server

```bash
uvicorn main:app --reload
```

## Health check

`GET /health`

Example response:

```json
{"status": "ok"}
```

Interactive API documentation is available at:
http://127.0.0.1:8000/docs
