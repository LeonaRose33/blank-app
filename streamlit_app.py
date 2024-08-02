import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
connection =st.secrets["DB_URI"]
with st.connection(**connection) as conn:
    query= f""" SELECT * FROM defaultdb """
    res = conn.query(query)
    if res:
        all_res = res.fetchall()
        st.write(all_res)