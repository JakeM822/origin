# demo_caller.py
from taskflow.tests.demo_tasks import parse_task, priority_score, sort_tasks

# Simulate what the rest of the app does with these functions
tasks = [
    parse_task({"title": "  Deploy API ", "priority": "HIGH"}),
    parse_task({"title": "Write docs",    "priority": "low"}),
    parse_task({"title": "Fix login bug", "priority": "high"}),
]
print("Parsed tasks:")
for t in tasks:
    print(" ", t)

print("\nSorted by priority:")
for t in sort_tasks(tasks):
    print(" ", t)