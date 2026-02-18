import streamlit as st

# Създаваме празен списък
if "books" not in st.session_state:
    st.session_state.books = []

# Полета за въвеждане
title = st.text_input("Заглавие")
author = st.text_input("Автор")

# Бутон за добавяне
if st.button("Добави книга"):
    book = {
        "title": title,
        "author": author
    }
    st.session_state.books.append(book)
    st.success("Книгата е добавена!")

# Показване на книгите
st.write("### Списък с книги:")
st.write(st.session_state.books)
