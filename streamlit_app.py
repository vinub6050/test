import streamlit as st
import openai

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
        with st.spinner("GPT-4.1 Mini 모델이 응답 중입니다..."):
            try:
                # OpenAI API를 통해 GPT-4.1 모델에 질문 전달 (스트리밍 사용)
                response = openai.Completion.create(
                    model="gpt-4.1-mini",  # GPT-4.1 Mini 모델을 사용합니다.
                    prompt=question,
                    max_tokens=150,  # 최대 토큰 수 (응답 길이)
                    temperature=0.7,  # 생성의 다양성
                    stream=True,  # 스트리밍을 활성화하여 실시간으로 응답 받기
                )

                # 응답을 스트리밍 방식으로 처리
                answer = ""
                for chunk in response:
                    if chunk.get("choices"):
                        text = chunk["choices"][0]["text"]
                        answer += text  # 실시간으로 텍스트 누적
                        st.write(text, end="")  # 실시간으로 출력
                st.subheader("GPT의 답변:")
                st.write(answer)  # 최종 누적된 응답 출력

            except openai.error.AuthenticationError:
                st.error("API Key가 잘못되었습니다. 다시 확인해주세요.")
            except openai.error.OpenAIError as e:
                st.error(f"API 호출 중 오류가 발생했습니다: {e}")
            except Exception as e:
                st.error(f"알 수 없는 오류가 발생했습니다: {e}")
else:
    st.info("API Key를 입력한 후 질문을 해주세요.")
