"""A small in-memory task API used in the Copilot course."""

from itertools import count

from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator

app = FastAPI(title="Course Task API", version="0.1.0")


class TaskCreate(BaseModel):
    """Fields accepted when creating a task."""

    title: str = Field(min_length=1, max_length=120)
    completed: bool = False

    @field_validator("title")
    @classmethod
    def title_must_contain_non_whitespace(cls, title: str) -> str:
        if not title.strip():
            raise ValueError("title must contain at least one non-whitespace character")
        return title


class Task(TaskCreate):
    """Task returned by the API."""

    id: int


_tasks: list[Task] = []
_task_ids = count(1)


@app.get("/healthz")
async def healthz() -> dict[str, str]:
    """Report that the service is running."""

    return {"status": "ok"}


@app.get("/tasks", response_model=list[Task])
async def list_tasks(completed: bool | None = None) -> list[Task]:
    """Return tasks currently held in memory, optionally filtered by completion."""

    if completed is None:
        return list(_tasks)
    return [task for task in _tasks if task.completed is completed]


@app.post("/tasks", response_model=Task, status_code=201)
async def create_task(request: TaskCreate) -> Task:
    """Create a task and store it in memory."""

    task = Task(id=next(_task_ids), **request.model_dump())
    _tasks.append(task)
    return task