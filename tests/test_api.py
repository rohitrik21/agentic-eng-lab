from pathlib import Path


def test_healthz_reports_service_is_running(client):
    response = client.get("/healthz")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_list_tasks_starts_empty(client):
    response = client.get("/tasks")

    assert response.status_code == 200
    assert response.json() == []


def test_create_task_defaults_to_incomplete(client):
    response = client.post("/tasks", json={"title": "Write API docs"})

    assert response.status_code == 201
    assert response.json() == {
        "id": 1,
        "title": "Write API docs",
        "completed": False,
    }


def test_created_task_appears_in_list(client):
    created = client.post(
        "/tasks",
        json={"title": "Review test feedback", "completed": True},
    )

    listed = client.get("/tasks")

    assert created.status_code == 201
    assert listed.status_code == 200
    assert listed.json() == [created.json()]


def test_readme_documents_task_api_contract():
    readme = (Path(__file__).resolve().parents[1] / "README.md").read_text(
        encoding="utf-8"
    )

    assert "`GET /healthz`" in readme
    assert '`200 OK` with `{"status": "ok"}`' in readme
    assert "`GET /tasks`" in readme
    assert "integer `id`, string `title`, and boolean `completed`" in readme
    assert "`POST /tasks`" in readme
    assert "required string `title` (1–120 characters)" in readme
    assert "optional boolean `completed` field (defaults to `false`)" in readme
    assert "`201 Created`" in readme
    assert "stored in memory and are lost when the service restarts" in readme