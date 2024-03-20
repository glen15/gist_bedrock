import streamlit as st
import boto3
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
    message_03_with_data = "아직 강의자료가 업데이트되지 않음"
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

    bedrock = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")
    response = bedrock.invoke_model(
        body=body, modelId="anthropic.claude-3-sonnet-20240229-v1:0"
    )
    response_body = json.loads(response.get("body").read())
    data = response_body.get("content")[0]
    ai_result = data["text"]

    send_message(f"{ai_result}", "ai")

    del bedrock
