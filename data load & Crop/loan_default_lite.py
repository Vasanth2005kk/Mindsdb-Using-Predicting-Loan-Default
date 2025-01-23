import pandas as pd

# File paths
input_file = '/home/vglug/Desktop/MindsDB-Loan-Prediction/Loan_Default.csv'      # Original file with 60000+ rows
output_file = '/home/vglug/Desktop/MindsDB-Loan-Prediction/loan_default_lite.csv'    # New file with 5000 rows

try:
    # Read the original CSV file
    df = pd.read_csv(input_file)

    # Extract the first 5000 rows
    df_chunk = df[:5000]

    # Save the first 5000 rows to the new file
    df_chunk.to_csv(output_file, index=False)

    # Remove the first 5000 rows from the original DataFrame
    df_remaining = df[5000:]

    # Save the remaining rows back to the original file
    df_remaining.to_csv(input_file, index=False)

    print(f"Successfully moved 5000 rows to '{output_file}' and updated '{input_file}'.")

except Exception as e:
    print(f"Error: {e}")
