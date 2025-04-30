import streamlit as st
import openai
pip install openai

# 앱 타이틀
st.title("GPT-4.1 Mini 웹 앱")

# 사용자로부터 OpenAI API Key 입력 받기
api_key = st.text_input("OpenAI API Key를 입력하세요:", type="password")

# API Key가 입력되었을 때만 질문을 받도록 하기
if api_key:
    openai.api_key = api_key

    # 사용자로부터 질문 입력 받기
    question = st.text_area("질문을 입력하세요:")

    # 질문이 입력되었을 때만 응답을 출력하도록 하기
    if question:
        try:
            # OpenAI API를 통해 GPT-4.1 모델에 질문 전달
            response = openai.Completion.create(
                model="gpt-4.1-mini",  # 모델 이름 (GPT-4.1 Mini 모델 사용)
                prompt=question,
                max_tokens=150,  # 최대 토큰 수 (응답 길이)
                temperature=0.7,  # 생성의 다양성
            )

            # 응답 출력
            answer = response.choices[0].text.strip()
            st.subheader("GPT의 답변:")
            st.write(answer)

        except openai.error.AuthenticationError:
            st.error("API Key가 잘못되었습니다. 다시 확인해주세요.")
        except openai.error.OpenAIError as e:
            st.error(f"API 호출 중 오류가 발생했습니다: {e}")
else:
    st.info("API Key를 입력한 후 질문을 해주세요.")
