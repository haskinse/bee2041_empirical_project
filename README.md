# Empirical Project – What makes a Taylor Swift song successful?

## Overview
This project examines what may drive the success of Taylor Swift’s music using track-level data. It combines multiple data sources and applies descriptive analysis, visualisation, and regression techniques to assess whether musical features are associated with success.

## Blog
The final blog can be accessed here:  
https://haskinse-bee2041empiricalproject.streamlit.app

## Project Structure

- .streamlit/  
  - configuration files and assets for the Streamlit app  

- data/  
  - raw/ original datasets (Kaggle, scraped data)  
  - clean/ cleaned datasets used for analysis  

- docs/  
  - images and files used in the blog  

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
2. Navigate into the project folder  
3. Install required packages:  
   pip install -r requirements.txt  
4. Run the Streamlit app:  
   streamlit run app.py  
5. The blog will open in your browser  

## Data Sources

- Album data: Wikipedia (web scraping)  
- Track features: Kaggle dataset – https://www.kaggle.com/datasets/gabyxd/taylor-swift-song-information  
- Listener data: Last.fm  
- Spotify data used for validation  

## Methods

- Data cleaning and merging  
- Descriptive statistics and visualisation  
- Correlation analysis  
- Multiple linear regression  

## Notes

- This project was primarily developed using Google Colab  
- The repository contains the cleaned data and outputs used in the final analysis  
- The source_code/ folder provides the scripts used for data processing and analysis  

- The analysis focuses on correlation rather than causal inference
