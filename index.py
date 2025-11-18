import streamlit as st

st.title("Streamlit 기본 실습")

# Task 1
st.subheader("Task 1: 기본 UI 컴포넌트")

# 입력 받을 텍스트(이름)
st.text_input("이름을 입력하세요")

# 나이 슬라이더
age = st.slider("나이", min_value=0, max_value=100)

# 좋아하는 색
color = st.selectbox("좋아하는 색", ["빨강", "초록", "파랑"])

# 체크박스
agree = st.checkbox("이용 약관에 동의합니다")

# 버튼
st.button("제출")



# Task5 
import pandas as pd

#title
st.title('Task5: 파일 업로드')

uploaded_file = st.file_uploader("Upload Your data", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.write("Uploaded Data")
    st.write(df)

