import streamlit as st
import pandas as pd

# Track4
st.write("### Task 4:인터랙티브 필터")

# st.file_uploader()를 사용하여 파일 업로더 위젯 생성
uploaded_file = st.file_uploader("CSV 파일을 선택하세요", type=["csv"])

if uploaded_file is not None:
    # 업로드된 파일이 있을 경우, pandas로 읽어 DataFrame 생성
    df = pd.read_csv(uploaded_file)
    st.write("업로드된 파일의 내용:")
    st.dataframe(df)
else:
    st.write("CSV 파일을 업로드해주세요.")