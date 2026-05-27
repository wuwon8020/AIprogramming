import streamlit as st
import Lab21_api
import Lab21_1
import Lab21_2
import Lab21_3
import Lab21_4
st.sidebar.title("Lab21 과제 웹페이지")

page = st.sidebar.radio(
    "실습 페이지 선택",
    (   "api_key 입력",
        "Lab21_1",
        "Lab21_2",
        "Lab21_3",
        "Lab21_4"
    )
)

if page == "api_key 입력":
    Lab21_api.app()

elif page == "Lab21_1":
    Lab21_1.app()

elif page == "Lab21_2":
    Lab21_2.app()

elif page == "Lab21_3":
    Lab21_3.app()
    
elif page == "Lab21_4":
    Lab21_4.app()
