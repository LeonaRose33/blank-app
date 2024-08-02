import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

conn = st.connection('sql_connection')
query= f""" SELECT * FROM defaultdb """
res = conn.query(query)
if res:
    st.dataframe(res)