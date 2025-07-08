import streamlit as st

main = st.Page("main.py", title="Principal", icon="😀")
second = st.Page("second.py", title="Secúndario", icon="😎")
third = st.Page("third.py", title="Terciário", icon="🙄")

pg = st.navigation([main, second, third])
pg.run()