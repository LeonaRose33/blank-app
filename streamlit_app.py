import streamlit as st
import mysql.connector

CONNECTION_DB = st.secrets["connectiondb"]

st.title("🎈 My DB Connection checking app")

with mysql.connector.connect(**CONNECTION_DB) as conn:
    #st.write(conn)
    cursor = conn.cursor()
    query = "SELECT * FROM capacities"
    st.write(f'Execute \n{query}')
    cursor.execute(query)
    results = cursor.fetchall()
    if results:
        columns = [col[0] for col in cursor.description]
        st.success('Query executed with SUCCESS')      
        st.dataframe(results, hide_index=False)

