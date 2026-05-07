# Empirical Project – What makes a Taylor Swift song successful?

## Overview
This project examines what may drive the success of Taylor Swift’s music using track-level data. It combines multiple data sources which have been cleaned and merged and uses statistical analysis, visualisation, and regression techniques to assess whether musical features are associated with success.

## Blog
The final blog can be accessed here:  
https://haskinse-bee2041empiricalproject.streamlit.app

## Project Structure

- .streamlit/  
  - configuration files and assets for the Streamlit app  

- data/  
  - raw/ original datasets (Kaggle, scraped data)  
  - clean/ cleaned datasets used for analysis  

- output/  
  - figures/ plots and charts  
  - regressions/ regression outputs  

- source_code/  
  - Python scripts for data collection, cleaning, and analysis  

- app.py  
  - main Streamlit app used to generate the final blog  

- requirements.txt  
  - required Python packages  

## How to Run the Project

1. Clone the repository  
2. Go into the project folder  
3. Install required packages:  
   pip install -r requirements.txt  
4. Run the Streamlit app:  
   streamlit run app.py  
5. The blog will open in your browser  

## Data Sources

- Album data: Wikipedia (web scraping)  
- Track features: Kaggle dataset – https://www.kaggle.com/datasets/gabyxd/taylor-swift-song-information  
- Listener data: Last.fm API 
- Spotify API data used for validation  

## Notes

- This project was primarily coded using Google Colab  
- The repository contains the raw and cleaned data, source code and outputs used in the final 
- The data collection code requires API access (Spotify and Last.fm), which is not included in this repository. To run this code apart from the rest of the project API keys must be generated and put into the code from Spotify for developers and the Last.fm API.
- Cleaned datasets are included, so the project can still be fully reproduced without re-running data collection 
