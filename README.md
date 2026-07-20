Crop Advisory Analytics Dashboard

A Data Analytics project that analyzes crop, soil, and climate data to help identify suitable crops based on environmental conditions. The project includes data cleaning, exploratory data analysis (EDA), interactive Power BI dashboards, and a simple crop recommendation system built using Python.

--> Project Overview
This project uses agricultural data containing:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- Soil pH
- Rainfall
- Crop Label

The objective is to analyze crop requirements, generate business insights, and recommend suitable crops based on soil and weather conditions.

-->Dashboard Preview
  [Dashboard](dashboard.png)

--> Features

- Data Cleaning using Pandas
- Exploratory Data Analysis (EDA)
- Interactive Power BI Dashboard
- Soil pH Analysis
- Rainfall Analysis
- NPK Comparison
- Crop Distribution Analysis
- Crop Recommendation based on user inputs

--> Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Power BI
- Google Colab

--> Project Structure

├── data/
│   ├── crop_data.csv
│   └── cleaned_crop_data.csv
│
├── Notebook/
│   └── projAgri.ipynb
│
├── dashboard.png
├── app.py
├── requirements.txt
└── README.md

--> Data Cleaning

The dataset was cleaned using Pandas by:
- Checking missing values
- Removing duplicate records
- Standardizing column names
- Exporting cleaned dataset for analysis

--> Exploratory Data Analysis

Performed analysis on:

- Crop Distribution
- Rainfall vs Temperature
- NPK Distribution
- Soil pH Distribution
- Correlation Heatmap

--> Power BI Dashboard

The dashboard provides:

- Average Temperature
- Average Rainfall
- Average Soil pH
- Crop Distribution
- Temperature Requirement by Crop
- Rainfall Requirement by Crop
- Soil pH Distribution
- NPK Comparison Across Crops

Interactive Filters:

- Crop Type
- Rainfall Range
- Temperature Range

--> Crop Recommendation Logic

A simple recommendation function filters crops based on:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- Soil pH
- Rainfall

It returns the most suitable crop using the mode of matching records.

Example:

```python
recommend_crop(90,40,40,25,80,6.5,200)

Output:
jute
```

--> Key Insights

- Average Temperature: **25.62°C**
- Average Rainfall: **103.46 mm**
- Average Soil pH: **6.47**
- Dataset contains **2200 agricultural records**
- Dashboard supports interactive filtering for better analysis

--> Dataset

Source:
Agricultural Crop Recommendation Dataset (Kaggle)

--> __Author__

*Badavath Madanlal*

- GitHub: https://github.com/badavathmadanlal
- LinkedIn: linkedin.com/in/badavathmadanlal
