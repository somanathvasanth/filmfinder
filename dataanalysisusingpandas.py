import pandas as pd
import os

# List all CSV files in the current directory
csv_files = [file for file in os.listdir('.') if file.endswith('.csv')]

# Read and analyze each CSV file
for file in csv_files:
    print(f"Analyzing {file}...")
    df = pd.read_csv(file)
    
    # Display basic information about the DataFrame
    print(f"Head of {file}:")
    print(df.head())
    print(f"Description of {file}:")
    print(df.describe())
    print(f"Info of {file}:")
    print(df.info())
    print("\n")