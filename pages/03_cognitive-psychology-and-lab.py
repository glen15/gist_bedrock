import streamlit as st
import requests
import json

file_path = "/home/ec2-user/environment/cognitive-psychology-and-lab.txt"

try:
    with open(file_path, "r", encoding="utf-8") as file:
        class_data = file.read()
except FileNotFoundError:
    class_data = ""

st.title("인지심리학 및 실험 : Cognitive-psychology-and-lab")
col1, col2 = st.columns(2)
with col1:
    st.image("cognitive-psychology-and-lab.jpeg", "인지심리학 및 실험", width=300)
with col2:
    st.image("choi.png", "최원일 교수님", width=100)


if "messages_03" not in st.session_state:
    st.session_state["messages_03"] = []


def send_message(message, role, save=True):
    with st.chat_message(role):
        st.write(message)
    if save:
        st.session_state["messages_03"].append({"message": message, "role": role})


for message in st.session_state["messages_03"]:
    send_message(
        message["message"],
        message["role"],
        save=False,
    )


message_03 = st.chat_input("수업에 관해 물어보세요!")
if class_data == "":
    message_03_with_data = "아직 강의자료가 업데이트되지 않았습니다."
    if message_03:
        send_message(message_03, "human")
        send_message(f"{message_03_with_data}", "ai")
else:
    message_03_with_data = (
        f"'{class_data}'에 기반해서 '{message_03}'내용에 대해서 답해라"
    )
    body = json.dumps(
        {
            "max_tokens": 1024,
            "messages": [{"role": "user", "content": message_03_with_data}],
            "anthropic_version": "bedrock-2023-05-31",
        }
    )
    if message_03:
        send_message(message_03, "human")

        # Lambda 함수 URL
        lambda_url = (
            "https://s4myrcprrekkd5mwfle5rc3nzu0nzobp.lambda-url.ap-northeast-2.on.aws/"
        )
        with st.spinner("잠시만 기다려 주세요..."):
            # HTTP POST 요청 보내기
            response = requests.post(lambda_url, json=body)

            # 응답 받기 및 처리
            if response.status_code == 200:
                response_data = response.json()
                ai_result = response_data["message"]
                send_message(ai_result, "ai")
            else:
                send_message("문제가 발생했습니다.", "ai")
