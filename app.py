import streamlit as st

st.title("What Makes a Taylor Swift Song Successful?")

st.write("This project explores whether musical features explain song success.")

st.image("output/figures/commercial_success/total_units_bar.png", caption="My chart")

if st.button("Show insight"):
    st.write("Higher energy songs tend to have more streams.")
