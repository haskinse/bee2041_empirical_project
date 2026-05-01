import streamlit as st

st.title("What Makes a Taylor Swift Song Successful?")

st.write("""Taylor Swift is one of the most successful music artists of all time. She’s sold over 100 million album units, multiple of her songs have passed one billion streams, and she’s the highest-grossing live music artist. But what actually drives her success? Is there something in the music itself that explains it, or is it something else entirely?

This blog looks at the musical features of her songs to see whether certain characteristics are linked to success. Are there patterns in which tracks become hugely popular while others don’t, or is her success about more than just the music?""")

st.subheader("Where did my data come from?")

st.write("""Taylor Swift is a good artist to study because there’s an unusually large amount of data available on her individual tracks. While platforms like Spotify no longer allow public access to detailed audio features such as tempo, key and energy, her dedicated fanbase means this information is still available at the song level. This allows for a much more detailed analysis than would be possible for most artists.

The data for this project comes from a mix of sources. Album-level success data was scraped from Wikipedia, while track-specific features were taken from a Kaggle dataset. Tracks were then standardised and matched with Spotify data to ensure accuracy, before being combined with play count and listener data from Last.fm.""")

st.subheader("What is 'success'?")

st.write("""It’s hard to definitively define what ‘success’ means for a musical artist, and therefore how it should be measured. There are a variety of possible metrics. Some are quantitative, such as commercial success or number of awards, while others are more qualitative, like cultural impact or recognition. For example, while Taylor Swift’s albums are often extremely commercially successful, it could be argued that other projects, such as Charli XCX’s Brat, have had a more intense cultural impact.

In this project, success is measured in two ways. At the album level, it is measured using units sold (from Wikipedia), while at the track level it is measured using listener and play counts from Last.fm. These metrics make success easier to quantify, and using multiple measures gives a more balanced view. However, this approach still has limitations, as it may miss more nuanced aspects of success, such as cultural impact or critical reception.""")

st.subheader("Which of Taylor Swift’s albums have been the most successful?")

st.write("""The most successful album by a clear margin is 1989, with just under 16 million certified units across the US and UK. Most of this comes from the original release, with a smaller contribution from the Taylor’s Version re release.

More broadly, album success looks fairly consistent across Swift’s career. While earlier albums tend to have higher total unit counts, they have also had more time to build up certifications. Because of this, it is hard to say that earlier music was necessarily more successful, as it may simply reflect how long it has been out.""")

st.image("output/figures/commercial_success/total_units_bar.png", caption="My chart")

st.subheader("Which of Taylor Swift’s songs have been the most successful?")

st.write("""Looking at individual tracks, a small number of songs dominate total listeners, while the majority receive far fewer. This creates a clear “long tail” pattern, where only a few songs become extremely large hits.

Among the very top songs, 1989 stands out in particular, although there is still a fairly balanced spread across albums overall. As before, older songs have had more time to build up listens, so this likely explains part of the pattern.""")

st.image("output/figures/commercial_success/top_20_track_listens.png", caption="My chart")

st.header("How have the muscial features of Taylor Swift’s music changed over time?")

feature = st.selectbox("Choose a musical feature:", ["Acousticness", "Danceability", "Duration in Minutes", "Energy", "Explicity", "Instrumentalness", "Liveness", "Loudness", "Speechiness", "Tempo", "Valence"])

if feature == "Acousticness":
    st.image("output/figures/track_feature_time/album_acousticness_time.png", width = 500)

elif feature == "Danceability":
    st.image("output/figures/track_feature_time/album_danceability_time.png", width = 500)

elif feature == "Duration in Minutes":
    st.image("output/figures/track_feature_time/album_duration_min_time.png", width = 500)

elif feature == "Energy":
    st.image("output/figures/track_feature_time/album_energy_time.png", width = 500)

elif feature == "Explicity":
    st.image("output/figures/track_feature_time/album_explicit_time.png", width = 500)

elif feature == "Instrumentalness":
    st.image("output/figures/track_feature_time/album_instrumentalness_time.png", width = 500)

elif feature == "Liveness":
    st.image("output/figures/track_feature_time/album_liveness_time.png", width = 500)

elif feature == "Loudness":
    st.image("output/figures/track_feature_time/album_loudness_time.png", width = 500)

elif feature == "Speechiness":
    st.image("output/figures/track_feature_time/album_speechiness_time.png", width = 500)

elif feature == "Tempo":
    st.image("output/figures/track_feature_time/album_tempo_time.png", width = 500)

elif feature == "Valence":
    st.image("output/figures/track_feature_time/album_valence_time.png", width = 500)
