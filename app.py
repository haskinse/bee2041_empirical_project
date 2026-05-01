import streamlit as st

st.title("What Makes a Taylor Swift Song Successful?")

st.write("""Taylor Swift is one of the most successful music artists of all time. She’s sold over 100 million album units, multiple of her songs have passed one billion streams, and she’s the highest-grossing live music artist. But what actually drives her success? Is there something in the music itself that explains it, or is it something else entirely?

This blog looks at the musical features of her songs to see whether certain characteristics are linked to success. Are there patterns in which tracks become hugely popular while others don’t, or is her success about more than just the music?""")

st.image("output/figures/commercial_success/total_units_bar.png", caption="My chart")

if st.button("Show insight"):
    st.write("Higher energy songs tend to have more streams.")
