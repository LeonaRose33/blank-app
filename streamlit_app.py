import streamlit as st
import mysql.connector
import pandas as pd

CONNECTION_DB = st.secrets["connectiondb"]

st.title("🎈 My DB Connection checking app")

with mysql.connector.connect(**CONNECTION_DB) as conn:
    #st.write(conn)
    cursor = conn.cursor()
    query = "SELECT * FROM capacities"
    st.write(f'Execute \n{query}')
    cursor.execute(query)
    st.success('Query executed with SUCCESS')
    results = cursor.fetchall()
    
if results:
    columns = [col[0] for col in cursor.description]
    df = pd.DataFrame(results, columns=columns)
    st.dataframe(df)
