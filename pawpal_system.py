from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import List
from collections import defaultdict


@dataclass
class Pet:
    name: str
    type: str
    tasks: List['Task'] = field(default_factory=list)

    def add_task(self, task: 'Task') -> None:
        self.tasks.append(task)


@dataclass
class Task:
    name: str
    time: datetime
    is_complete: bool = False

    def mark_complete(self) -> None:
        self.is_complete = True


class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        self.pets.append(pet)

    def remove_pet(self, pet: Pet) -> None:
        self.pets.remove(pet)

    def get_all_tasks(self) -> List['Task']:
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.tasks)
        return all_tasks


class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def schedule_task(self, task: 'Task', time: datetime) -> None:
        task.time = time

    def get_daily_schedule(self) -> List['Task']:
        tasks = self.owner.get_all_tasks()
        return sorted(tasks, key=lambda t: t.time.time())

    def check_conflicts(self, tasks: List['Task']) -> List[str]:
        conflicts = []
        time_to_tasks = defaultdict(list)
        for task in tasks:
            time_to_tasks[task.time].append(task)
        for time, task_list in time_to_tasks.items():
            if len(task_list) > 1:
                task_names = [t.name for t in task_list]
                conflicts.append(f"Conflict at {time.strftime('%H:%M')}: {', '.join(task_names)}")
        return conflicts