import streamlit as st

# ----------- INITIAL BOOK DATABASE -----------
books = [
    "The Hobbit",
    "1984",
    "Pride and Prejudice",
    "To Kill a Mockingbird",
    "The Great Gatsby"
]

# ----------- APP TITLE -----------
st.title("📚 Book Checker App")
st.write("Enter a book title to check if it exists in the database.")

# ----------- USER INPUT -----------
user_input = st.text_input("Book Title")

# ----------- CHECK BUTTON -----------
if st.button("Check Book"):
    if user_input.strip() == "":
        st.warning("Please enter a book title.")
    elif user_input in books:
        st.success("The book exists in the database!")
    else:
        st.error("The book is NOT in the database.")
