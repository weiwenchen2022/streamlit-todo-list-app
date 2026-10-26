import streamlit as st
from task_list import TaskList

if "task_list" not in st.session_state:
    st.session_state.task_list = TaskList()
    for name in ("Clean garage", "Finalize project proposal", "Buy bread"):
        st.session_state.task_list.add_task(name)


task_list: TaskList = st.session_state.task_list


with st.sidebar:
    task = st.text_input("Enter a task")
    if st.button("Add task", type="primary"):
        task_list.add_task(task)

st.metric(
    "Task completion",
    f"{sum(1 for task in task_list if task.is_done)} /  {len(task_list)} done",
    delta=None,
)

st.header("Today's to-dos:", divider="gray")
# st.info(f"task_list: {task_list=}")
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
