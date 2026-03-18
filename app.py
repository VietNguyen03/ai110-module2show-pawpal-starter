from datetime import datetime

from pawpal_system import Owner, Pet, Task, Scheduler
import streamlit as st


st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

# Initialize Owner and Scheduler in session_state to persist across refreshes
if "owner" not in st.session_state:
    st.session_state.owner = Owner("Jordan")

if "scheduler" not in st.session_state:
    st.session_state.scheduler = Scheduler(st.session_state.owner)

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

if st.button("Add Pet"):
    st.session_state.owner.add_pet(Pet(pet_name, species))
    st.success("Pet added successfully!")

st.markdown("### Tasks")
st.caption("Add a few tasks to a specific pet.")

if st.session_state.owner.pets:
    pet_names = [p.name for p in st.session_state.owner.pets]
    selected_pet_name = st.selectbox("Select Pet", options=pet_names)

    col1, col2, col3 = st.columns(3)
    with col1:
        task_title = st.text_input("Task title", value="Morning walk")
    with col2:
        duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
    with col3:
        priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

    if st.button("Add task"):
        # Find the actual pet object that matches the name in the dropdown
        target_pet = next(p for p in st.session_state.owner.pets if p.name == selected_pet_name)
        
        #convert the string "12:00" into a real datetime object
        try:
            task_time=datetime.strptime("12:00", "%H:%M")


            # Create the Task object with real date time
            new_task = Task(name=task_title, time=task_time) 
        
            # Add it to the pet's list
            target_pet.tasks.append(new_task)
            st.success(f"Added '{task_title}' to {selected_pet_name}!")
        except ValueError:
            st.error("Invalid time format. Please use HH:MM format.")
else:
    st.info("Add a pet above before you can add tasks.")

st.divider()

st.subheader("Build Schedule")

if st.button("Generate schedule"):
    # Call your scheduler logic from pawpal_system.py
    full_schedule = st.session_state.scheduler.get_daily_schedule()
    conflicts = st.session_state.scheduler.check_conflicts(full_schedule)
    
    if full_schedule:
        st.write("### Today's Schedule")
        for task in full_schedule:
            status = "✅" if task.is_complete else "⏳"
            st.write(f"{status} **{task.time.strftime('%H:%M')}**: {task.name}")
    else:
        st.info("No tasks scheduled yet! Make sure you added tasks to your pets.")
    
    if conflicts:
        st.warning("⚠️ Schedule Conflicts Detected:")
        for conflict in conflicts:
            st.write(f"- {conflict}")
    else:
        st.success("✅ No scheduling conflicts!")