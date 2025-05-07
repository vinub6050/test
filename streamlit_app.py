cd my-chatbot-app  # streamlit_app.py 있는 폴더로 이동

git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/your-username/streamlit-chatbot.git
git push -u origin main


# streamlit_app.py
import streamlit as st
import openai

st.set_page_config(page_title="GPT 챗봇", page_icon="🤖")

st.title("🧠 OpenAI GPT 챗봇")

# API 키 입력
api_key = st.text_input("🔑 OpenAI API Key", type="password")

if api_key:
    openai.api_key = api_key
    prompt = st.text_area("💬 질문을 입력하세요", height=200)

    if st.button("🚀 질문하기", disabled=(len(prompt.strip()) == 0)):
        try:
            with st.spinner("GPT가 생각 중입니다..."):
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",  # 또는 "gpt-4" (유료 계정)
                    messages=[{"role": "user", "content": prompt}]
                )
                st.success("🎉 응답 도착!")
                st.markdown(response["choices"][0]["message"]["content"])
        except Exception as e:
            st.error(f"❌ 오류 발생: {e}")
else:
    st.info("먼저 OpenAI API 키를 입력하세요.")

