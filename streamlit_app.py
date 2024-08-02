import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

conn = st.connection(name='sql_connection', type='sql')
query= f"""SELECT capacity FROM capacities"""
st.write(conn)
st.write(query)
st.help()
cursor = conn.cursor()
st.write(cursor)
res = cursor.execute(query)
st.write(res)