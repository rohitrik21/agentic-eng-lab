# agentic-eng-lab

A small in-memory Task API built with FastAPI.

## Requirements

- Python 3.10 or later
- FastAPI 0.115 or later, below 1.0
- Uvicorn 0.30 or later, below 1.0

## Install

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

## Run

```bash
uvicorn app.main:app --reload
```

The API is available at `http://127.0.0.1:8000`. Interactive API documentation is at `http://127.0.0.1:8000/docs`.

## Endpoints

- `GET /healthz` — Returns `{"status": "ok"}`.
- `GET /tasks` — Lists tasks. Optionally pass `completed=true` or `completed=false` to filter by completion status.
- `POST /tasks` — Creates a task. Provide a JSON body with a required `title` (1–120 characters) and optional `completed` boolean (defaults to `false`). Returns the task, including its assigned integer `id`, with status `201 Created`.

Tasks are stored in memory and are lost when the service restarts.