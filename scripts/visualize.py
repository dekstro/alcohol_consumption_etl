import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data(data):
    try:
        # Histogram of total alcohol consumption
        plt.figure(figsize=(10, 6))
        sns.histplot(data['Total_Consumption'], kde=True, color='blue')
        plt.title('Distribution of Total Alcohol Consumption per Capita')
        plt.xlabel('Total Consumption')
        plt.ylabel('Frequency')
        plt.savefig('../output/total_consumption_histogram.png')

        # Bar chart for average consumption of each type
        avg_consumption = data[['Beer_Per_Capita', 'Wine_Per_Capita', 'Spirits_Per_Capita', 'Other_Per_Capita']].mean()
        avg_consumption.plot(kind='bar', color=['gold', 'red', 'green', 'purple'])
        plt.title('Average Consumption of Beer, Wine, Spirits, and Others')
        plt.ylabel('Consumption per Capita')
        plt.savefig('../output/average_consumption_bar_chart.png')

        print("Visualizations generated successfully.")
    except Exception as e:
        print(f"Error during visualization: {e}")
