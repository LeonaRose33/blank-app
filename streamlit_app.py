import streamlit as st
import sqlalchemy

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

try: 
    with st.connection('sql_connection', type='sql') as conn:
        query= f""" SELECT * FROM defaultdb """
        res = conn.query(query)
        if res:
            st.write(res)
except Exception as e:
    st.write(e)