import pandas as pd

def transform_data(data):
    try:
        # Handle missing values
        data.dropna(inplace=True)

        # Pivot the data: Create separate columns for each beverage type
        pivot_data = data.pivot_table(
            index=['Year', 'WHO Region', 'Country'],
            columns='Beverage Types',
            values='Display Value',
            aggfunc='sum'
        ).reset_index()

        # Rename columns for clarity
        pivot_data.rename(
            columns={
                'Beer': 'Beer_Per_Capita',
                'Wine': 'Wine_Per_Capita',
                'Spirits': 'Spirits_Per_Capita',
                'Other': 'Other_Per_Capita'
            },
            inplace=True
        )

        # Fill NaN values with 0 (countries may lack data for some beverages)
        pivot_data.fillna(0, inplace=True)

        # Calculate Total Alcohol Consumption
        pivot_data['Total_Consumption'] = (
            pivot_data['Beer_Per_Capita'] +
            pivot_data['Wine_Per_Capita'] +
            pivot_data['Spirits_Per_Capita'] +
            pivot_data['Other_Per_Capita']
        )

        print("Data transformed successfully.")
        return pivot_data

    except Exception as e:
        print(f"Error during data transformation: {e}")
        return None
