import streamlit as st
import Lab21_api
from openai import OpenAI

def app():
    # session_state 초기화  
    
    # 캐시 함수
    @st.cache_data
    def get_response(prompt, api_key):

        # 함수 내부에서 client 생성
        client = OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    # 사용자 입력
    prompt = st.text_area("질문 입력")

    if st.button("실행"):
        if not st.session_state.api_key:
            st.error("api 페이지에서 api키를 입력해주세요!")
            st.stop()

        if not prompt:
            st.warning("질문을 입력하세요.")
            st.stop()

        answer = get_response(prompt, st.session_state.api_key)

        st.write("응답:")
        st.write(answer)