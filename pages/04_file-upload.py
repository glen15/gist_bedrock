import streamlit as st
import os

st.title("파일 업로드")
uploaded_file = st.file_uploader("강의자료 파일을 업로드 해주세요.")

if uploaded_file is not None:
    content = uploaded_file.getvalue()
    
    save_path = '/home/ec2-user/environment'
    file_name = uploaded_file.name


    complete_path = os.path.join(save_path, file_name)

    with open(complete_path, "wb") as f:
        f.write(content)

    st.success('File successfully saved')
