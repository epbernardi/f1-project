# f1-project
This project automates the extraction, processing, and visualization of historical Formula 1 data. Using Python, web scrapping and Streamlit, it collects detailed information about races, drivers, teams, and fastest laps, transforming them into interactive charts and tables for an insightful analysis of the sport.

#  F1 Data Dashboard  

This project collects, processes, and visualizes historical Formula 1 data, allowing users to explore interactive statistics on races, drivers, teams, and fastest laps over the years.  

## Technologies Used  
- **Python** → Data extraction, processing, and analysis  
- **Playwright** → Browser automation for web scraping  
- **Pandas** → Data manipulation and processing  
- **Streamlit** → Interactive dashboard creation  
- **Plotly** → Dynamic data visualizations  

## Features  
- Automated data extraction from **1950 to the present year**  
- Interactive rankings of drivers and teams by season  
- Analysis of fastest laps and race times  
- Comparison of statistics across F1 history  
- Intuitive interface for data exploration  

## How to Use  

### 1 Install dependencies  

pip install -r requirements.txt


### 2 Run the script to collect data

python formula1.py


### 3 Run the jupyter notebbok to adjuste all data

python formula1_data.ipynb


### 4 Start the interactive dashboard

streamlit run dashboar.py



# PROJECT STRUCTURE

f1-data-dashboard/
│── formula1.py             # Web scraping script for data extraction
│── formula1_data.ipynb      # Jupyter Notebook for data processing and analysis
│── dashboard.py             # Streamlit interactive dashboard
│── requirements.txt         # Project dependencies
│── data/                    # Folder where CSV files are stored



Feel free to contribute with suggestions, improvements, or new features!
