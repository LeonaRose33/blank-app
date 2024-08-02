import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

conn = st.connection('sql_connection', 'sql')
query= f"""SELECT * FROM capacities"""
st.write(conn)
st.write(query)
res = conn.query(query)
st.write(res)