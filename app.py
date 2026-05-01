import streamlit as st

st.title("What Makes a Taylor Swift Song Successful?")

st.write("""Taylor Swift is one of the most successful music artists of all time. She’s sold over 100 million album units, multiple of her songs have passed one billion streams, and she’s the highest-grossing live music artist. But what actually drives her success? Is there something in the music itself that explains it, or is it something else entirely?

This blog looks at the musical features of her songs to see whether certain characteristics are linked to success. Are there patterns in which tracks become hugely popular while others don’t, or is her success about more than just the music?""")

st.subheader("Where did my data come from?")

st.write("""Taylor Swift is a good artist to study because there’s an unusually large amount of data available on her individual tracks. While platforms like Spotify no longer allow public access to detailed audio features such as tempo, key and energy, her dedicated fanbase means this information is still available at the song level. This allows for a much more detailed analysis than would be possible for most artists.

The data for this project comes from a mix of sources. Album-level success data was scraped from Wikipedia, while track-specific features were taken from a Kaggle dataset. Tracks were then standardised and matched with Spotify data to ensure accuracy, before being combined with play count and listener data from Last.fm.""")

st.image("output/figures/commercial_success/total_units_bar.png", caption="My chart")

if st.button("Show insight"):
    st.write("Higher energy songs tend to have more streams.")
