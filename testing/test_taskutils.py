import pytest
from app.task_utils import parse_task, InvalidTaskError


def test_parse_task_valid_returns_normalized():
    # Arrange
    record = {"title": " Ship ", "priority": "HIGH"}
    # Act
    result = parse_task(record)
    # Assert
    assert result == {"title": "Ship", "priority": "high", "done": False}


def test_parse_task_missing_title_raises():
    with pytest.raises(InvalidTaskError):
        parse_task({})


def test_parse_task_whitespace_title_raises():
    with pytest.raises(InvalidTaskError):
        parse_task({"title": "   "})

@pytest.fixture
def sample_tasks():
    return [
        {"title": "Deploy", "priority": "high", "done": False},
        {"title": "Docs", "priority": "low", "done": False},
    ]


def test_high_priority_filter(sample_tasks):
    from app.task_utils import high_priority_titles
    assert high_priority_titles(sample_tasks) == ["Deploy"]

