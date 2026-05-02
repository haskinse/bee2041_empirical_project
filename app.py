import streamlit as st

st.set_page_config(page_title = "What Makes a Taylor Swift Song Successful?", page_icon = "🎵")

st.title("What Makes a Taylor Swift Song Successful?")

st.write("""Taylor Swift is one of the most successful music artists of all time. She’s sold over 100 million album units, multiple of her songs have passed one billion streams, and she’s the highest-grossing live music artist. But what actually drives her success? Is there something in the music itself that explains it, or is it something else entirely?

This blog looks at the musical features of her songs to see whether certain characteristics are linked to success. Are there patterns in which tracks become hugely popular while others don’t, or is her success about more than just the music?""")

st.divider()

st.header("Where did my data come from?")

st.write("""Taylor Swift is a good artist to study because there’s an unusually large amount of data available on her individual tracks. While platforms like Spotify no longer allow public access to detailed audio features such as tempo, key and energy, her dedicated fanbase means this information is still available at the song level. This allows for a much more detailed analysis than would be possible for most artists.

The data for this project comes from a mix of sources. Album-level success data was scraped from Wikipedia, while track-specific features were taken from a Kaggle dataset. Tracks were then standardised and matched with Spotify data to ensure accuracy, before being combined with play count and listener data from Last.fm.""")

st.divider()

st.header("How should we define success?")

st.write("""It’s hard to definitively define what ‘success’ means for a musical artist, and therefore how it should be measured. There are a variety of possible metrics. Some are quantitative, such as commercial success or number of awards, while others are more qualitative, like cultural impact or recognition. For example, while Taylor Swift’s albums are often extremely commercially successful, it could be argued that other projects, such as Charli XCX’s Brat, have had a more intense cultural impact.

In this project, success is measured in a number of ways. At the album level, it is measured using certified units and total sales. As a rough proxy for cultural impact wikipedia page length it utilised, although this only gives a rough idea. At the track level success is measured using listener and play counts from Last.fm. These metrics make success easier to quantify, and using multiple measures gives a more balanced view. However, this approach still has limitations, as it may miss more nuanced aspects of success, such as critical reception.""")

st.divider()

st.header("Which of Taylor Swift’s albums have been the most successful?")

st.write("""The most successful album by a clear margin is 1989, with just under 16 million certified units across the US and UK. Most of this comes from the original release, with a smaller contribution from the Taylor’s Version re release.

More broadly, album success looks fairly consistent across Swift’s career. While earlier albums tend to have higher total unit counts, they have also had more time to build up certifications. Because of this, it is hard to say that earlier music was necessarily more successful, as it may simply reflect how long it has been out.""")

metric = st.segmented_control("Choose success measure:", ["Units", "Sales", "Wikipedia Page Length"], default = "Units")

if metric == "Units":
    st.image("output/figures/commercial_success/total_units_bar.png", use_container_width=True)

elif metric == "Sales":
    st.image("output/figures/commercial_success/total_sales_bar.png", use_container_width=True)

elif metric == "Wikipedia Page Length":
    st.image("output/figures/commercial_success/page_length_bar.png", use_container_width=True)
    
st.divider()

st.header("Which songs have the most listeners?")

st.write("""Looking at individual tracks, a small number of songs dominate total listeners, while the majority receive far fewer. This creates a clear “long tail” pattern, where only a few songs become extremely large hits.

Among the very top songs, 1989 stands out in particular, although there is still a fairly balanced spread across albums overall. As before, older songs have had more time to build up listens, so this likely explains part of the pattern.""")

top_n = st.slider("Choose how many top songs to show:", min_value = 10, max_value = 220, value = 20, step = 10, key = "top_tracks_slider")

st.image(f"output/figures/commercial_success/top_tracks/top_{top_n}_track_listens.png")

st.divider()

st.header("How have the musical features of Taylor Swift’s music changed over time?")

st.write("""Taylor Swift is often described as a “chameleon” because she’s constantly shifting her sound and genre. Her earlier albums, like Taylor Swift and Fearless, are clearly country, while albums like 1989 and Red move much more into pop. More recent work explores indie, folk-pop and alternative styles.

However, when you look at measurable track features, her music is often more consistent over time than this might suggest.""")

feature = st.selectbox("Choose a musical feature:", ["Acousticness", "Danceability", "Duration in Minutes", "Energy", "Explicit", "Instrumentalness", "Liveness", "Loudness", "Speechiness", "Tempo", "Valence"], key = "track_feature_time_selectbox")

if feature == "Acousticness":
    st.image("output/figures/track_feature_time/track_acousticness_time.png")

elif feature == "Danceability":
    st.image("output/figures/track_feature_time/track_danceability_time.png")

elif feature == "Duration in Minutes":
    st.image("output/figures/track_feature_time/track_duration_min_time.png")

elif feature == "Energy":
    st.image("output/figures/track_feature_time/track_energy_time.png")

elif feature == "Explicit":
    st.image("output/figures/track_feature_time/track_explicit_time.png")

elif feature == "Instrumentalness":
    st.image("output/figures/track_feature_time/track_instrumentalness_time.png")

elif feature == "Liveness":
    st.image("output/figures/track_feature_time/track_liveness_time.png")

elif feature == "Loudness":
    st.image("output/figures/track_feature_time/track_loudness_time.png")

elif feature == "Speechiness":
    st.image("output/figures/track_feature_time/track_speechiness_time.png")

elif feature == "Tempo":
    st.image("output/figures/track_feature_time/track_tempo_time.png")

elif feature == "Valence":
    st.image("output/figures/track_feature_time/track_valence_time.png")

st.divider()

st.header("How are these features related to success?")

st.write("To explore whether musical features influence popularity, I plotted each feature against track success, measured using log listeners. If certain features consistently made songs more successful, these graphs should show clear upward or downward patterns.")

feature = st.selectbox("Choose a musical feature:", ["Acousticness", "Danceability", "Duration in Minutes", "Energy", "Explicit", "Instrumentalness", "Liveness", "Loudness", "Speechiness", "Tempo", "Valence"], key = "track_feature_success_selectbox")

if feature == "Acousticness":
    st.image("output/figures/track_feature_success/track_acousticness_success.png")

elif feature == "Danceability":
    st.image("output/figures/track_feature_success/track_danceability_success.png")

elif feature == "Duration in Minutes":
    st.image("output/figures/track_feature_success/track_duration_min_success.png")

elif feature == "Energy":
    st.image("output/figures/track_feature_success/track_energy_success.png")

elif feature == "Explicit":
    st.image("output/figures/track_feature_success/track_explicit_success.png")

elif feature == "Instrumentalness":
    st.image("output/figures/track_feature_success/track_instrumentalness_success.png")

elif feature == "Liveness":
    st.image("output/figures/track_feature_success/track_liveness_success.png")

elif feature == "Loudness":
    st.image("output/figures/track_feature_success/track_loudness_success.png")

elif feature == "Speechiness":
    st.image("output/figures/track_feature_success/track_speechiness_success.png")

elif feature == "Tempo":
    st.image("output/figures/track_feature_success/track_tempo_success.png")

elif feature == "Valence":
    st.image("output/figures/track_feature_success/track_valence_success.png")

st.divider()

st.header("How correlated are muscial features?")

st.image("output/figures/correlation_matrices/track_features_success.png")

st.divider()

st.header("Multiple Linear Regression")

st.image("output/figures/regressions/scaled_track_coefficients.png")

