import streamlit as st
import functions


# Function to add a new to-do item to the list of todos
def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)  # Add new to-do item to the list
    functions.write_todos(todos)  # Write updated list to file
    st.session_state['new_todo'] = ''  # Clear the new_todo variable from the text box


todos = functions.get_todos()  # Get list of todos from file

# Create the title of the app
st.title("My To-Do App")

# Loop through all the todos and create a checkbox for each one
for index, item in enumerate(todos):
    checkbox = st.checkbox(item, key=item)  # Create a checkbox with the current todo item
    if checkbox:
        todos.pop(index)  # Remove the item from the list if checkbox is checked
        functions.write_todos(todos)  # Write updated list to file
        del st.session_state[item]  # Delete the session state of the item
        st.experimental_rerun()  # Rerun the app to reflect the changes


# Create a text input box for the user to add a new todo item
st.text_input(label="", placeholder="Enter a todo...",
              on_change=add_todo, key='new_todo')   # Key is used to access the input box
