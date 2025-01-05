import pymysql
import db_config

def load_data(data):
    try:
        # Connect to MySQL
        connection = pymysql.connect(**db_config)
        cursor = connection.cursor()

        # Create table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS alcohol_consumption (
            Year INT,
            WHO_Region VARCHAR(255),
            Country VARCHAR(255),
            Beer_Per_Capita FLOAT,
            Wine_Per_Capita FLOAT,
            Spirits_Per_Capita FLOAT,
            Other_Per_Capita FLOAT,
            Total_Consumption FLOAT
        );
        """
        cursor.execute(create_table_query)

        # Insert data
        for _, row in data.iterrows():
            sql = """
            INSERT INTO alcohol_consumption (
                Year, WHO_Region, Country, Beer_Per_Capita, Wine_Per_Capita,
                Spirits_Per_Capita, Other_Per_Capita, Total_Consumption
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
            """
            cursor.execute(sql, tuple(row))

        connection.commit()
        print("Data loaded into MySQL successfully.")

    except Exception as e:
        print(f"Error during data load: {e}")

    finally:
        cursor.close()
        connection.close()
