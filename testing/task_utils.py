from __future__ import annotations
import os
import text_utils



ALLOWED_PRIORITIES = {"low", "medium", "high"}

class InvalidTaskError(ValueError):
    pass
    
def parse_task(record: dict) -> dict:
    title = record.get("title", "").strip()
    if not title:
        raise InvalidTaskError("Task record cannot be empty.")
    priority = record.get("priority", "medium").strip()
    if priority not in {"low", "medium", "high"}:
        priority = "medium"
    if len(title.strip()) > 200:
        raise InvalidTaskError("Task title cannot exceed 200 characters.")
    return {"title": title, "priority": priority, "done": False}

def high_priority_titles(tasks:list[dict]) -> list[str]:
    return [task["title"] for task in tasks if task["priority"] == "high"]

def priority_score(priority: str) -> int:
    """Return a numeric weight for sorting tasks by priority."""
    weights = {"low": 1, "medium": 2, "high": 3}
    return weights.get(priority, 0)

def sort_tasks(tasks: list[dict]) -> list[dict]:
    """Return tasks ordered by priority, highest first."""
    return sorted(tasks, key=lambda t: priority_score(t["priority"]), reverse=True)

def add_tag(tag, tags=None):
    if tags is None:
        tags = []
    tags.append(tag)
    return tags
##if no default argument is provided, create a new list

def load_dotenv():
    os.environ.get("DATABASE_URL")

class Task:
    def __init__(self, title: str, priority: str = "medium"):
        self.title = title
        self.priority = priority
        self.done = False

    def complete(self) -> None:
        self.done = True

    def __repr__(self) -> str:
        return f"Task(title={self.title!r}, priority={self.priority!r}, done={self.done})"


if __name__ == "__main__":
    sample_records = [
        {"title": "  Ship the release  ", "priority": "high"},
        {"title": "Write unit tests", "priority": "medium"},
        {"title": "Clean up code", "priority": "low"},
    ]

    parsed_tasks = [parse_task(record) for record in sample_records]
    print("Parsed tasks:")
    print(parsed_tasks)

    sorted_tasks = sort_tasks(parsed_tasks)
    print("Sorted tasks (high → low):")
    print(sorted_tasks)

    print("Priority scores:")
    print([priority_score(task["priority"]) for task in sorted_tasks])

    sample_tags = add_tag("urgent")
    print("Tags after first add_tag:")
    print(sample_tags)

    more_tags = add_tag("important", sample_tags)
    print("Tags after adding important:")
    print(more_tags)

    try:
        print(parse_task({"title": "", "priority": "URGENT"}))
    except InvalidTaskError as e:
        print(f"Error: {e}")
