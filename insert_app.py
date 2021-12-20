import streamlit as st
from mysql_connection import get_connection
from logging import currentframe
import mysql.connector
from mysql.connector import errors
from datetime import datetime


def run_insert_app():
    st.subheader('회원가입')

    email = st.text_input('이메일 입력')
    password = st.text_input('비번입력',type='password',max_chars=12)
    age = st.number_input('나이 입력', min_value= 1)
    address = st.text_input('주소입력')

    if st.button('저장하기'):
        try :
        # 1. DB 연결
            connection = get_connection()

            # 2. 쿼리문 만들기
            query ='''insert into test_user(email, password, age, address) values(%s, %s, %s, %s);'''

            record= (email, password, age, address)
            # 3. 커넥션으로부터 커서를 가져온다.
            cursor = connection.cursor()
            # 4. 쿼리문을 커서에 넣어서 실행한다.
            cursor.execute(query, record)
            # 5. 커넥션을 커밋한다 DB에 영구적으로 반영한다.
            connection.commit()

        except errors as e :
            print('Error', e)
        finally :
            if connection.is_connected() :
                cursor.close()
                connection.close()
                print('MySQL connectionis closed')
                st.write('회원 정보가 저장되었습니다.')