# Empirical Project – What makes a Taylor Swift song successful?

## Overview
This project explores what drives the success of Taylor Swift’s music using track-level data. It combines multiple data sources and applies descriptive analysis, visualisation, and regression techniques to examine whether musical features are linked to success.

## Blog / Output
You can view the final blog here:  
https://haskinse-bee2041empiricalproject.streamlit.app

## Project Structure

- .streamlit/  
  - configuration files and assets for the Streamlit app  

- data/  
  - raw/ # original datasets (Kaggle, scraped data)  
  - clean/ # cleaned datasets used for analysis  

- docs/  
  - images and files used in the blog  

- output/  
  - figures/      # plots and charts  
  - regressions/  # regression outputs  

- source_code/  
  - Python scripts for data cleaning, analysis, and visualisation  

- app.py  
  - main Streamlit app used to generate the final blog  

- requirements.txt  
  - required Python packages  

- README.md  
  - project documentation and replication instructions  

## How to Run the Project

1. Clone the repository:  
   git clone https://github.com/YOUR-USERNAME/bee2041_empirical_project.git  

2. Navigate into the folder:  
   cd bee2041_empirical_project  

3. Install required packages:  
   pip install -r requirements.txt  

4. Run the Streamlit app:  
   streamlit run app.py  

5. The blog will open in your browser.

## Data Sources

- Album data: Wikipedia (web scraping)  
- Track features: Kaggle dataset  
- Listener data: Last.fm  
- Spotify data used for validation  

## Methods

- Data cleaning and merging  
- Descriptive statistics and visualisation  
- Correlation analysis  
- Multiple linear regression  

## Notes

- This project was primarily developed using Google Colab  
- The code has been exported and organised into this repository for replication  
- The Streamlit app (app.py) uses the processed data and outputs generated during this workflow  
- To fully reproduce all intermediate steps, running the scripts in the source_code/ folder (or re-running them in a notebook environment such as Colab) may be helpful  

- The project focuses on correlation rather than causal inference  
- Results may be affected by omitted variable bias  
- Data has been pre-processed for consistency across sources
