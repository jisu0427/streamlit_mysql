import streamlit as st
import mysql.connector


def run_insert_app():
    st.subheader('회원가입')

    email = st.text_input('이메일 입력')
    password = st.text_input('비번입력',type='password',max_chars=12)
    age = st.number_input('나이 입력', min_value= 1)
    address = st.text_input('주소입력')

