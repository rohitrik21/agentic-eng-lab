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

- `GET /healthz` — Returns `200 OK` with `{"status": "ok"}`.
- `GET /tasks` — Returns `200 OK` with a JSON array of tasks. Each task has an integer `id`, string `title`, and boolean `completed` field. Optionally pass `completed=true` or `completed=false` to filter by completion status.
- `POST /tasks` — Accepts a JSON object with a required string `title` (1–120 characters) and an optional boolean `completed` field (defaults to `false`). The title must contain at least 1 and at most 120 characters. On success, returns `201 Created` with the created task: an integer `id`, string `title`, and boolean `completed`.

Tasks are stored in memory and are lost when the service restarts.