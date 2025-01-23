from mindsdb_sdk import connect

# Connect to MindsDB server
server = connect("http://127.0.0.1:47334/")  # Replace with your IP if needed
project = server.get_project("mindsdb")

# Create and train a model using the dataset directly
model = project.create_model(
    name="loan_prediction_model",
    from_data="/home/vglug/Desktop/MindsDB-Loan-Prediction/Loan_Default.csv",  # Path to CSV
    to_predict="Loan_Default"  # Replace with your actual target column
)

# Wait until the model is trained
model.wait()

# Output model training status
print("Model training complete:", model.info())

