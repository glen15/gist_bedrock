import streamlit as st


st.set_page_config(
    page_title="GIST with Bedrock",
    page_icon="🤖",
)



st.title("광주과학기술원(GIST) : Bedrock Demo")
st.markdown(
    """
    ### [강의자료 업로드 페이지](/file-upload)
    """
    )
st.divider()
col1, col2 = st.columns(2)
with col1:
    st.image("gist.svg", "광주과학기술원", width=200)

with col2:
    st.markdown(
        """
    # GIST 수업 목록
                
    ### ["미래 반도체"](/semiconductors)
    ### ["지구수문학"](/earth-hydrology)
    ### ["인지심리학 및 실험"](/cognitive-psychology-and-lab)
    """
    )
st.divider()