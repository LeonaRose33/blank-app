import streamlit as st
import mysql.connector

connectiondb = st.secrets["connectiondb"]

with mysql.connector.connect(**connectiondb) as conn:
    st.write(conn)
    cursor = conn.cursor()
    query = "SELECT * FROM capacities"
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
