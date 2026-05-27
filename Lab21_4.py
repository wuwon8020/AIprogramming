from openai import OpenAI
import streamlit as st

def app() :
    st.title("ChatPDF")
    if "api_key" not in st.session_state or not st.session_state.api_key:
        st.error("api 페이지에서 api키를 입력해주세요!")
        st.stop()
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "name" in st.session_state:
        st.write(st.session_state["name"])
    
    
    uploaded_file = st.file_uploader(
        "pdf 파일을 첨부하세요",
        type= "pdf"
    )

    if uploaded_file is not None:
        st.success("파일 업로드 완료")
    
    @st.cache_data
    def get_response(messages, api_key, file):
        client = OpenAI(api_key=api_key)
        openai_file = client.files.create(
        file=uploaded_file,
        purpose="user_data"
        )
        response = client.responses.create(
            model="gpt-5.4-mini",
            input=[{
            "role": "user",
            "content": 
            [{"type": "input_file", "file_id": openai_file.id,},
            {"type": "input_text", "text" : f"{messages}"} ]
            }]
        )

        return response.output_text
    
    if st.button("clear"):
        st.session_state.messages = []
        st.rerun()

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        
        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })

        with st.chat_message("user"):
            st.markdown(prompt)
        api_messages = [
            {
                "role": "system",
                "content": f"""
너는 입력받은 pdf에 근거해서만 답변하는 챗봇이다.
사용자의 질문에 대해 아래 pdf에서 관련 내용을 찾아 답변하라.
pdf에 없는 내용은 'pdf에서 확인할 수 없습니다'라고 답하라.
"""
            }
        ] + st.session_state.messages

        response = get_response(api_messages, st.session_state.api_key, uploaded_file)
    
        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })

        with st.chat_message("assistant"):
            st.markdown(response)
