import streamlit as st
import Lab21_api
from openai import OpenAI


def app() :
# session_state 초기화
    if not st.session_state.api_key:
        st.error("api 페이지에서 api키를 입력해주세요!")
        st.stop()
    if "name" in st.session_state:
        st.write(st.session_state["name"])

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