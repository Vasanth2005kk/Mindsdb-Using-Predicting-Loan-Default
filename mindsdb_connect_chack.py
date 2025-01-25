from mindsdb_sdk import connect

# Connect to MindsDB server
server = connect("http://172.17.0.1:47334/")  # Replace with your IP if needed
project = server.get_project("mindsdb")

model = project.list_models()[0]

print(model)

