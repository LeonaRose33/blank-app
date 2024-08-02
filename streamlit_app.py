import streamlit as st
import os


import streamlit as st
import pandas as pd
import mysql.connector

connectiondb = st.secrets['connectiondb']

with mysql.connector.connect(**connectiondb) as conn:
    cursor = conn.cursor()
    query = "SELECT capacity FROM capacities"
    print(f'Execute \n{query}')
    cursor.execute(query)
    results = cursor.fetchall()
    if results:
        columns = [col[0] for col in cursor.description]
        print('Query executed with SUCCESS')      
        st.dataframe(results)

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

conn = st.connection(name='sql_connection', type='sql')
query= f"""SELECT capacity FROM capacities"""
st.write(conn)
st.write(query)
res = conn.query(query)
st.write(res)