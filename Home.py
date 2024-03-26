import streamlit as st


st.set_page_config(
    page_title="SEOULTECH with Bedrock",
    page_icon="🤖",
)


st.title("서울과학기술대학교 : Bedrock Demo")
st.markdown(
    """
    ### [강의자료 업로드 페이지](/file-upload)
    """
)
st.divider()
col1, col2 = st.columns(2)
with col1:
    st.image("seoultech.png", "서울과학기술대학교", width=200)

with col2:
    st.markdown(
        """
    # 수업 목록
                
    ### ["미래 반도체"](/semiconductors)
    ### ["지구수문학"](/earth-hydrology)
    ### ["인지심리학 및 실험"](/cognitive-psychology-and-lab)
    """
    )
st.divider()
