import streamlit as st
from openai import OpenAI



# session_state 초기화
if "api_key" not in st.session_state:
    st.session_state.api_key = ""

# API Key 입력
st.session_state.api_key = st.text_input(
    "OpenAI API Key 입력",
    type="password",
    value=st.session_state.api_key
)

if "messages" not in st.session_state:
    st.session_state.messages = []

# 캐시 함수
@st.cache_data
def get_response(messages, api_key):

    # 함수 내부에서 client 생성
    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )

    return response.choices[0].message.content

# 사용자 입력
prompt = ""
if st.button("clear"):
    st.session_state.messages = []
    st.rerun()


if prompt := st.chat_input("What is up?"):
# 사용자 메시지 보여주기
    st.chat_message("user").markdown(prompt)
# 메모리에 사용자 메시지 저장
    st.session_state.messages.append({"role": "user", "content": prompt})
# LLM 응답 가져오는 기능 추가 필요
    answer = get_response(st.session_state.messages, st.session_state.api_key)
    response = f"Echo: {answer}"
# LLM 응답 보여주기
    with st.chat_message("assistant"):
        st.markdown(response)
# 메모리에 LLM 응답 저장
    st.session_state.messages.append({"role": "assistant", "content": response})