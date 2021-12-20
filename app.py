import streamlit as st


from insert_app import run_insert_app

def main():
    # CRUD 라고 한다.
    # Create, Read, Update, Delete 
    menu = ['Insert','Select','Update','Delete']
    choice = st.sidebar.selectbox('선택하세요', menu)

    if choice == 'Insert':
        run_insert_app()

    elif choice == 'Select':
        pass

    elif choice == 'Update':
        pass

    elif choice == 'Delete':
        pass

if __name__ == '__main__':
    main()