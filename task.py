from typing import NamedTuple, Self


class Task(NamedTuple):
    name: str
    is_done: bool = False

    def mark_done(self) -> Self:
        return self._replace(is_done=True)

    def mark_not_done(self) -> Self:
        return self._replace(is_done=False)
