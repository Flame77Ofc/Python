import streamlit as st

pages = st.navigation([
    st.Page("main.py", title="Principal", icon="😀"),
    st.Page("second.py", title="Secúndario", icon="😎"),
    st.Page("third.py", title="Terciário", icon="🙄")
])

pages.run()