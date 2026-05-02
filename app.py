import streamlit as st

st.set_page_config(page_title = "What Makes a Taylor Swift Song Successful?", page_icon = "🎵")

st.title("What Makes a Taylor Swift Song Successful?")
st.write("Taylor Swift is one of the most successful music artists of all time. She’s sold over 100 million album units, multiple songs have passed one billion streams, and she’s the highest-grossing live music artist. But what actually drives that success? Is it something in the music itself, or is it something else entirely?")
st.write("This blog looks at the musical features of her songs to see whether certain characteristics are linked to success. More specifically, it focuses on correlation rather than causation, asking whether patterns in the data can help explain why some tracks perform better than others.")
st.image("IMG_0511.jpeg")

st.divider()

st.header("Where did my data come from?")
st.write("Taylor Swift is a great artist to study because there’s an unusually large amount of data available on her individual tracks. While platforms like Spotify no longer allow public access to detailed audio features such as tempo, key and energy, her dedicated fanbase means this information is still available at the song level. That makes a much more detailed analysis possible than for most artists.")
st.write("The data for this project comes from a mix of sources. Album-level success data was scraped from Wikipedia, while track features were taken from a Kaggle dataset. Tracks were then standardised and matched with Spotify data to improve consistency, before being combined with play count and listener data from Last.fm.")

st.divider()

st.header("How should we define success?")
st.write("It’s hard to pin down what “success” actually means for a musical artist, and therefore how to measure it. There are lots of possible metrics. Some are quantitative, like sales or awards, while others are more qualitative, like cultural impact or recognition. For example, while Taylor Swift’s albums are often extremely commercially successful, you could argue that other projects, like Charli XCX’s Brat, have had a stronger cultural impact.")
st.write("In this project, success is measured in a few different ways. At the album level, it’s based on certified units and total sales. As a rough proxy for cultural impact, Wikipedia page length is also used, although this is only an approximation. At the track level, success is measured using listener and play counts from Last.fm.")
st.write("Using multiple measures makes success easier to quantify and gives a more balanced view. That said, it still has limitations, as it can miss more nuanced aspects like critical reception.")


st.divider()

st.header("Which of Taylor Swift’s albums have been the most successful?")
st.write("Taylor Swift’s most commercially successful album, by both sales and certified units, is 1989, followed by her second album, Fearless. When combined with the re-released Taylor’s Version, 1989 has over 20 million certified units and around $10 million in certified sales.")
st.write("Looking at Wikipedia page length instead, Folklore comes out on top, although it’s closely followed by 1989. This suggests that despite slightly weaker commercial performance, Folklore may have had a stronger cultural impact or at least generated more discussion.")
st.write("The most striking feature of the data, though, is how consistent her success has been across her career. Even her lowest-performing album, Evermore, still has over four million certified units, going 4× platinum in the United States. Unlike many other artists, Swift has largely avoided a true “flop era.")
    
metric = st.segmented_control("Choose success measure:", ["Units", "Sales", "Wikipedia Page Length"], default = "Units")

if metric == "Units":
    st.image("output/figures/commercial_success/total_units_bar.png", use_container_width=True)

elif metric == "Sales":
    st.image("output/figures/commercial_success/total_sales_bar.png", use_container_width=True)

elif metric == "Wikipedia Page Length":
    st.image("output/figures/commercial_success/page_length_bar.png", use_container_width=True)
    
st.divider()

st.header("Which songs have the most listeners?")
st.write("Unsurprisingly, the most popular songs tend to come from her most successful albums, with six of the top ten coming from 1989 and Fearless. Her most popular song by far, with around 1.8 million listeners, is Blank Space. Interestingly, two of the top ten come from Folklore, one of her less commercially successful albums, which highlights how strong her catalogue is overall.")
st.image("output/figures/commercial_success/top_tracks/top_10_track_listeners_table.png")
st.write("Looking at listener numbers across all of her songs, this consistency becomes even clearer. While there are standout tracks like Blank Space, most of her songs sit in a fairly tight range, with roughly 500,000 to 1,000,000 listeners. The spread of albums across the top-performing tracks reinforces this, showing that her success isn’t limited to just one era.")      
top_n = st.slider("Choose how many top songs to show:", min_value = 10, max_value = 220, value = 20, step = 10, key = "top_tracks_slider")
st.image(f"output/figures/commercial_success/top_tracks/top_{top_n}_track_listens.png")

st.divider()

st.header("How have the musical features of Taylor Swift’s music changed over time?")
st.write("Taylor Swift is often described as a “chameleon” because she’s constantly shifting her sound and genre. Her earlier albums, like Taylor Swift and Fearless, are clearly country, while albums like 1989 and Red move much more into pop. More recent work explores indie, folk-pop and alternative styles.")
st.write("However, when you look at measurable track features, her music is more consistent over time than this might suggest. Key metrics like danceability, tempo and valence do vary between albums, but there’s no clear overall trend.")
st.write("There are a couple of exceptions. The share of explicit tracks has increased in more recent albums, particularly from Folklore onwards. Acousticness also shows the biggest shifts between albums, reflecting how she moves between more stripped-back, acoustic sounds and more produced, studio-heavy tracks.")

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
st.write("In this case, log listeners are used as a measure of track success. Looking across the different musical features, most of the trend lines are close to flat, with no clear pattern suggesting that any one characteristic consistently drives success.")
st.write("This points to a broader idea: Taylor Swift’s success doesn’t seem to come from any single feature. Instead, it’s likely the result of a combination of factors, many of which aren’t fully captured by these audio metrics alone.")

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
st.write("Looking at correlation coefficients between musical features and log listeners confirms what the graphs suggested: relationships are very weak, with values ranging from around -0.13 to 0.17. There’s no strong linear relationship between any single feature and success.")
st.write("Looking at correlations between the features themselves, more expected patterns show up. Energy and loudness are strongly positively correlated, while loudness and acousticness are strongly negatively correlated. This is important for the regression, as high correlation between explanatory variables can make it harder to isolate their individual effects.")
st.image("output/figures/correlation_matrices/track_features_success.png")

st.divider()

st.header("Multiple Linear Regression")
st.write("Running the regression, the standardised coefficients are very small, ranging from around -0.04 to 0.06. This suggests that musical features on their own do not explain much of the variation in song success.")
st.write("To balance interpretability and completeness, a smaller baseline model is used alongside a more extended specification. While the baseline model focuses on a few key features, the extended model includes a wider set of variables as a robustness check. In both cases, the overall conclusion remains the same: the relationships are weak.")
st.write("It’s also important to be clear about the limitations of this approach. With only around 220 tracks, the dataset is relatively small, and there is a risk of omitted variable bias. Factors such as marketing, playlist placement, and broader cultural context are not included in the model, but are likely to influence success. If these omitted factors are correlated with the included audio features, the estimated coefficients may be biased.")
st.image("output/figures/regressions/scaled_track_coefficients.png")

st.divider()

st.header("Conclusions")
st.write("Overall, there’s very little evidence that any single musical feature drives the success of a Taylor Swift song. Across the analysis, relationships between features and listener numbers are consistently weak, and even when combining multiple variables in a regression, the effects remain small.")
st.write("Instead, her success looks much more consistent and widespread. Both at the album and track level, there isn’t really a clear divide between “hits” and “failures”, but rather a large number of songs that all perform well. This suggests that her success is less about specific characteristics of individual songs, and more about broader factors.")
st.write("These likely include timing, marketing, fanbase strength, and cultural relevance, none of which are fully captured by the data used here. More importantly, even if stronger statistical relationships were found, this would not necessarily imply causality without a more robust research design.")
st.write("Ultimately, Taylor Swift’s success doesn’t seem to come down to any one feature or formula. If anything, the consistency across her catalogue suggests that it’s the combination of factors around the music, rather than the measurable properties of the music itself, that matters most.")
