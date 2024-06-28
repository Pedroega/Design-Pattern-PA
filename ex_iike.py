"""
Example of IIKE (Information, Initialization, Knowledge, Execution) pattern:
This example demonstrates a data processing workflow using the IIKE pattern. 
The process includes collecting information from a CSV file, initializing variables, 
applying business logic to filter and calculate the average of values, and finally 
executing the task of saving the processed data to a new CSV file.
"""

import pandas as pd

class IIKE:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        self.processed_data = None

    def information(self):
        print("Collecting information from the file...")
        try:
            self.data = pd.read_csv(self.file_path)
            print("Information collected successfully!")
        except FileNotFoundError:
            print("File not found.")
            self.data = None

    def initialization(self):
        print("Initializing variables...")
        if self.data is not None:
            self.processed_data = pd.DataFrame()
            print("Variables initialized successfully!")
        else:
            print("Failed to initialize variables due to lack of data.")

    def knowledge(self):
        print("Applying business logic...")
        if self.data is not None:
            # Example of business logic: filter and calculate the average of a column
            self.processed_data = self.data[self.data['value'] > 10].copy()
            self.processed_data.loc[:, 'average'] = self.processed_data['value'].mean()
            print("Business logic applied successfully!")
        else:
            print("Failed to apply business logic due to lack of data.")

    def execution(self):
        print("Executing main task...")
        if self.processed_data is not None and not self.processed_data.empty:
            output_file = 'processed_data.csv'
            self.processed_data.to_csv(output_file, index=False)
            print(f"Main task executed successfully! Data saved in {output_file}")
        else:
            print("Failed to execute main task due to lack of processed data.")

    def run(self):
        self.information()
        self.initialization()
        self.knowledge()
        self.execution()

# Usage
file_path = 'data.csv'  # Make sure this file exists and contains a 'value' column (example csv file in folder)
iike = IIKE(file_path)
iike.run()
