from collections.abc import Iterable
from dataclasses import dataclass, field

from task import Task


@dataclass
class TaskList:
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, name: str) -> None:
        self.tasks.append(Task(name))

    def delete_task(self, idx: int) -> None:
        del self.tasks[idx]

    def mark_done(self, idx: int) -> None:
        self.tasks[idx] = self.tasks[idx].mark_done()

    def mark_not_done(self, idx: int) -> None:
        self.tasks[idx] = self.tasks[idx].mark_not_done()

    def __iter__(self) -> Iterable[Task]:
        yield from self.tasks

    def __len__(self) -> int:
        return len(self.tasks)
