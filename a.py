import streamlit as st

st.title("はじめてのStreamlit")

name = st.text_input("名前を入力")
age = st.number_input("年齢", min_value=0, max_value=120)

if st.button("送信"):
    st.write(f"{name}さんは {age} 歳です")


