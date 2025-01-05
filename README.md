# alcohol_consumption_etl
This repository contains the average consumption of alcohol across countries over the years
# ETL Pipeline for Alcohol Consumption Analysis

## Objective
Analyze global alcohol consumption data, identify patterns, and visualize trends using Python and MySQL.

## Features
- ETL pipeline to extract, transform, and load alcohol consumption data.
- Statistical modeling of beer, wine, and spirits consumption.
- Visualizations to showcase patterns and trends.

## Technologies
- **Python**: Data processing and visualization
- **MySQL**: Data storage and analysis
- **Matplotlib/Seaborn**: Visualization
- **Pandas**: Data manipulation

## Steps to Run
1. Install dependencies: install required packages - pandas,pymysql,matplotlib,seaborn
2. Place your dataset in the `data` folder.
3. Configure your database credentials in `db_config.py`.
4. Run the pipeline: `python scripts/main.py`

## Output
- Transformed data loaded into MySQL database.

## Visualizations
- Histogram of total alcohol consumption per capita.
- Bar chart for average consumption of beer, wine, and spirits.
