import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
secret = st.secrets.items()
st.write(st.secrets["DB_USERNAME"])
st.write(st.secrets["DB"])
