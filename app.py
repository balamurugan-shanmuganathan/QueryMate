import os
import streamlit as st
import pandas as pd
from user_codes.agents import pandas_dataframe_agent, sql_db_exec, sql_agent

def main():

    st.set_page_config(page_title="QueryMate", layout="wide")
    
    st.title("QueryMate")
    st.markdown("### Friendly assistant for querying your data")
    file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])
    agent_list = ['Pandas Dataframe Agent', 'SQL Agent']
    agent_type = st.sidebar.selectbox("Select Agent Type", agent_list)
    submit = st.sidebar.button("Upload")

    st.session_state.setdefault("submitted", False)
    st.session_state.setdefault("data", False)
    st.session_state.setdefault("response", False)
    st.session_state.setdefault("my_db", False)

    if submit:
        if not file:
            st.stop()
        data = pd.read_csv(file) 
        my_db = sql_db_exec(data)
        st.success("File uploaded successfully!")
        st.session_state.submitted = True
        st.session_state.data = data
        st.session_state.my_db = my_db

    if st.session_state.submitted:  
        if st.button("show your data"):
            st.dataframe(st.session_state.data.head())
        
        # Initialize chat history
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = []

        for chat_history in st.session_state.chat_history:
            with st.chat_message(chat_history["role"]):
                st.markdown(chat_history["content"])

        if prompt := st.chat_input("Enter your query"):
            # Display the user messages in chat message container
            with st.chat_message("user"):
                st.markdown(prompt)
            # Add user message into chat history
            st.session_state.chat_history.append({"role":"user", "content":prompt})

            if agent_type == 'Pandas Dataframe Agent':
                response = pandas_dataframe_agent(st.session_state.data, prompt)
                st.session_state.response = response

            elif agent_type == 'SQL Agent':
                response = sql_agent(st.session_state.my_db, prompt)
                st.session_state.response = response

            
            with st.chat_message("assistant"):
                st.markdown(response)
            # Add assistant response to chat history
            st.session_state.chat_history.append({"role":"assistant", "content":st.session_state.response})


if __name__ == "__main__":
    main()