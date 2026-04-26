import streamlit as st

st.title("Mirësevini në Aplikacionin tim Streamlit")
st.write("Ky është një shembull i thjeshtë i një aplikacioni Streamlit.")

name = st.text_input("Shkruani emrin tuaj:")
if name:
    st.write(f"Përshëndetje, {name}!")