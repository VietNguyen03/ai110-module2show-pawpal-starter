from pawpal_system import Owner, Pet, Task, Scheduler
from datetime import datetime

# Create an owner
owner = Owner("John Doe")

# Create two pets
pet1 = Pet("Buddy", "Dog")
pet2 = Pet("Whiskers", "Cat")

# Add pets to owner
owner.add_pet(pet1)
owner.add_pet(pet2)

# Create feeding tasks
task1 = Task("Feeding", datetime.now())
task2 = Task("Feeding", datetime.now())

# Add tasks to pets
pet1.add_task(task1)
pet2.add_task(task2)

# Create scheduler
scheduler = Scheduler(owner)

# Get and print daily schedule
daily_schedule = scheduler.get_daily_schedule()
print("Daily Schedule:")
for task in daily_schedule:
    print(f"- {task.name} for {task.time} (Complete: {task.is_complete})")
