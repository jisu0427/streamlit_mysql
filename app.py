import streamlit as st


from insert_app import run_insert_app
from select_app import run_select_app
from update_app import run_update_app

def main():
    # CRUD 라고 한다.
    # Create, Read, Update, Delete 
    menu = ['Insert','Select','Update','Delete']
    choice = st.sidebar.selectbox('선택하세요', menu)

    if choice == 'Insert':
        run_insert_app()
    elif choice == 'Select':
        run_select_app()
    elif choice == 'Update':
        run_update_app()

if __name__ == '__main__':
    main()