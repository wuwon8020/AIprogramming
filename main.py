import streamlit as st
import Lab21
import Lab21_2

st.sidebar.title("메뉴")

page = st.sidebar.radio(
    "페이지 선택",
    (
        "Page1",
        "Page2",
        "Page3",
        "Page4"
    )
)

if page == "Page1":
    Lab21.app()

elif page == "Page2":
    Lab21_2.app()
