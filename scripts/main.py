from extract import extract_data
from transform import transform_data
from load import load_data
from visualize import visualize_data

def main():
    # File path
    file_path = "D:/alcohol_consumption_etl/data/world_alcohol_comsumption.csv"

    # Step 1: Extract
    raw_data = extract_data(file_path)

    if raw_data is not None:
        # Step 2: Transform
        transformed_data = transform_data(raw_data)

        if transformed_data is not None:
            # Step 3: Load
            load_data(transformed_data)

            # Step 4: Visualize
            visualize_data(transformed_data)

if __name__ == "__main__":
    main()
