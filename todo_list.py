import streamlit as st
from jokes import generate_joke
from task_list import TaskList

if "task_list" not in st.session_state:
    st.session_state.task_list = TaskList()
    for name in ("Clean garage", "Finalize project proposal", "Buy bread"):
        st.session_state.task_list.add_task(name)


if "joke" not in st.session_state:
    api_key = st.secrets["jokes_api"]["api_key"]
    st.session_state.joke = generate_joke(api_key)

task_list: TaskList = st.session_state.task_list


with st.sidebar:
    task = st.text_input("Enter a task")
    if st.button("Add task", type="primary"):
        task_list.add_task(task)

st.info(st.session_state.joke)

st.metric(
    "Task completion",
    f"{sum(1 for task in task_list if task.is_done)} /  {len(task_list)} done",
    delta=None,
)

st.header("Today's to-dos:", divider="gray")
for idx, task in enumerate(task_list):
    task_col, delete_col = st.columns([0.8, 0.2])
    with task_col:
        label = f"~~{task.name}~~" if task.is_done else task.name
        checked = st.checkbox(label, task.is_done, key=f"task_{idx}")
        if checked and not task.is_done:
            task_list.mark_done(idx)
            st.rerun()
        elif not checked and task.is_done:
            task_list.mark_not_done(idx)
            st.rerun()

    with delete_col:
        if st.button("Delete", key=f"delete_{idx}"):
            task_list.delete_task(idx)
            st.rerun()
