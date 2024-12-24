import streamlit as st
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
import os
import sqlite3
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType
from langchain.sql_database import SQLDatabase
from langchain_core.prompts import PromptTemplate

os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp')

def pandas_dataframe_agent(data, prompt):    
    agent= create_pandas_dataframe_agent(llm, data, verbose=True, allow_dangerous_code=True)
    return agent.run(prompt)

def sql_db_exec(data):
    sqllite_connection = sqlite3.connect('data.db')
    data.to_sql('listing', sqllite_connection, if_exists = 'replace')
    my_db = SQLDatabase.from_uri('sqlite:///data.db')
    return my_db

def sql_agent(my_db, prompt):

    # Create the SQLDatabaseToolkit with the required LLM
    toolkit = SQLDatabaseToolkit(llm=llm, db=my_db)

    lc_agent_executor = create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        handle_parsing_errors=True,
        verbose=True,
        return_intermediate_steps=True,
    )

    template = PromptTemplate(
    input_variables = ['user_query', 'backround_info'],
    template = """{backround_info}

        Question: {prompt}

        """
    )

    backround_info = """
        You are a SQL expert integrated with a database system. When you receive query results, you need to summarize them for the user in simple terms.

        If the query results contain numeric values (e.g., averages or counts), present them in 
        a user-friendly manner. Do not say "I don't know" unless the database query fails or no data 
        is returned.

        if you have multiple line shown in points
        """

    # return lc_agent_executor.run(template.format(backround_info = backround_info, prompt = prompt))
    return lc_agent_executor.run(prompt)