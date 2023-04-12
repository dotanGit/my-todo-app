import streamlit as st
import functions


def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state['new_todo'] = ''  # clear the new_todo variable
    st.session_state['textbox'] = ''  # clear the textbox value on the website


todos = functions.get_todos()

st.title("My To-Do App")

for index, item in enumerate(todos):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[item]
        st.experimental_rerun()


st.text_input(label="", placeholder="Enter a todo...",
              on_change=add_todo, key='new_todo')