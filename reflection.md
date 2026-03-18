# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?
### My initial design used a modular approach with four classes: Owner, Pet, Task and Scheduler.
### Owner manages the list of pets; Pet hold specific task data; Task handles individual activity details( time, name, duration); and Scheduler acts as the engine to organize all tasks into a single timeline.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.
### I originally didn't have a duration attribute for tasks. I added it during implementation because I realized a schedule isn't helpful if you don't know how long an activity ( for ex like a 30 min walk) will take.


---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?
### My scheduler considers Time as the primary constraint and pet ownership a the secondary constraint.
### Time mattered most because a schedule is fundamentally a chronological sequence; without proper timing, a pet owner wouldn't know the order of operations for their day.
**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?
### My scheduler currently allows conflicts but flags them with a warning.
### This is a reasonable tradeoff because it gives the human owner the final say. Instead of the code "deleting" a task automatically, it alerts the user so they can manually adjust their plans
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?
### I used AI for design brainstorming (creating the UML with Mermaid.js), generating code skeletons, and debugging specific errors like indentation issues.
### The most helpful prompts were specific ones, like asking it to "Update the Scheduler class to sort tasks by time using a lambda function.
**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?
### There was a moment where the AI suggested using a variable (selected_pet_name) in the backend before I had actually built the dropdown menu in the Streamlit UI
### I didn't accept the code as-is; I had to pause and first build the UI component to ensure the variable actually existed before the logic could run.
---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
### I tested Task Creation, Chronological Sorting, and Conflict Detection.
- Why were these tests important?
### These were important to ensure that "Breakfast" at 8:00 AM always appears before "Dinner" at 6:00 PM, and that the user is warned if they try to do two things at once


**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?
### I am very confident in the sorting logic.
### If I had more time, I would test Edge Cases like "Overnight Tasks" (tasks that start at 11:00 PM and end at 1:00 AM) to see how the scheduler handles date changes.
---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
### I am most satisfied with the Streamlit integration. Seeing the Python logic I wrote actually appear as a working app in the browser was very rewarding.
**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
### I would redesign the Task class to include "Categories" (e.g., Health vs. Fun) so that the schedule could be color-coded for better readability.
**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
### Double check Co pilot code before keeping the changed code.