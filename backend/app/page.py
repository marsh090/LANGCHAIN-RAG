import streamlit as st

def create_page(app):
    st.title("Drinkye")
    st.write("Welcome to Drinkye, the AI bartender!")
    st.write("Please enter your drink request below:")
    
    if st.button("Generate Drink"):
        response = app.generate_drink(drink_request)
        st.write(response)
    st.write("Drinkye will generate a drink recipe for you based on your request!")

    st.write("Please enter your drink request below:")
    drink_request = st.text_input("Drink Request")