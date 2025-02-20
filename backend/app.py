from app.create_db import create_app
from app.page import create_page

import streamlit as st

# Create app instance
app = create_app()

# Set up Streamlit page configuration
st.set_page_config(page_title="Drinkye", page_icon=":cocktail:")

# Create and display the page
page = create_page(app)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=3033)