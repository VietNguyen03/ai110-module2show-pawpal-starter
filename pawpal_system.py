from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class Pet:
    name: str
    type: str
    tasks: List['Task'] = field(default_factory=list)

    def add_task(self, task: 'Task') -> None:
        pass


@dataclass
class Task:
    name: str
    time: datetime
    status: str

    def mark_complete(self) -> None:
        pass


class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        pass

    def remove_pet(self, pet: Pet) -> None:
        pass


class Scheduler:
    def schedule_task(self, task: 'Task', time: datetime) -> None:
        pass