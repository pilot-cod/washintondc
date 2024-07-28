import json
import streamlit as st
import requests

# Streamlit UI for data input
st.title('DIET CHUNG STUDENT MANAGEMENT SYSTEM')

# Set the title of the app
st.title("Welcome, student")

# Display a simple greeting
st.write("Login")

# Add some interactivity with a button
is_clicked =  st.button('Click me')

# Add a text input
user_input = st.text_input("Enter your name")

# =================== LOGIC

def send_request(user_input):
  url = 'http://127.0.0.1:5000/login'  # Replace with your Flask app's URL

  headers = {'Content-Type': 'application/json'}
  data = { "name" : user_input }
  response = requests.post(url, data=json.dumps(data), headers=headers)
  if response.status_code == 200:
    res_data = response.json()
    print(res_data)
    accepted = res_data['accepted']
    if accepted:
        st.success('Hello, DC student!')
    else:
        st.error('You\'re not in the list, please buy you  weapon and comeback!')
    return True
  else:
      st.error('Error making prediction')

if is_clicked:
  st.write(user_input)
  send_request(user_input)