import streamlit as st

st.title("📚 Book Manager App")

# ------------------ SESSION STATE ------------------
if "books" not in st.session_state:
    st.session_state.books = []

# ------------------ ADD BOOK SECTION ------------------
st.header("➕ Add a New Book")

title = st.text_input("Title")
author = st.text_input("Author")

if st.button("Add Book"):
    if title.strip() == "" or author.strip() == "":
        st.warning("Please enter both title and author.")
    else:
        book = {
            "title": title.strip(),
            "author": author.strip()
        }
        st.session_state.books.append(book)
        st.success("Book added successfully!")

# ------------------ DISPLAY BOOK LIST ------------------
st.header("📖 Book List")

if st.session_state.books:
    for i, book in enumerate(st.session_state.books, start=1):
        st.write(f"{i}. {book['title']} by {book['author']}")
else:
    st.info("No books added yet.")

# ------------------ CHECK BOOK SECTION ------------------
st.header("🔍 Check if a Book Exists")

search_title = st.text_input("Enter book title to search")

if st.button("Check Book"):
    if search_title.strip() == "":
        st.warning("Please enter a book title.")
    else:
        exists = any(
            book["title"].lower() == search_title.strip().lower()
            for book in st.session_state.books
        )

        if exists:
            st.success("The book exists in the database!")
        else:
            st.error("The book is NOT in the database.")
