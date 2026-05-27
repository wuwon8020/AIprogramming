import streamlit as st
from openai import OpenAI


def app():
    # session_state 초기화

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if not st.session_state.api_key:
        st.error("api 페이지에서 api키를 입력해주세요!")
        st.stop()

    if "name" in st.session_state:
        st.write(st.session_state["name"])

    @st.cache_data
    def get_response(messages, api_key):
        client = OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=messages
        )

        return response.choices[0].message.content

    if st.button("clear"):
        st.session_state.messages = []
        st.rerun()

    # 핵심 1: 이전 채팅 UI에 다시 출력
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # 새 사용자 입력
    if prompt := st.chat_input("What is up?"):

        # 핵심 2: 사용자 메시지를 session_state에 저장
        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })

        with st.chat_message("user"):
            st.markdown(prompt)

        # 핵심 3: 이전 대화 전체를 프롬프트로 전달
        answer = get_response(
            st.session_state.messages,
            st.session_state.api_key
        )

        # Echo 빼는 게 자연스러움
        response = answer

        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })

        with st.chat_message("assistant"):
            st.markdown(response)