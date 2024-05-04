from flask import Flask, request, jsonify
import requests
import time
import threading
import mysql.connector
import boto3
import json

app = Flask(__name__)

# Function to retrieve database credentials from AWS Secrets Manager
def get_database_credentials():
    # Create a Secrets Manager client
    secrets_manager_client = boto3.client('secretsmanager', region_name='your_region')

    # Retrieve the secret containing database credentials
    secret_name = 'your_secret_name'
    response = secrets_manager_client.get_secret_value(SecretId=secret_name)
    secret = json.loads(response['SecretString'])

    return secret

# Function to make REST calls and store data in the Aurora database
def make_rest_calls_and_store(endpoint, frequency, duration):
    total_calls = frequency * duration
    calls_made = 0
    
    # Retrieve database credentials
    db_config = get_database_credentials()

    # Connect to the Aurora database
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    while calls_made < total_calls:
        response = requests.get(endpoint)
        data = response.json()  # Assuming the response is in JSON format
        
        # Insert data into the database
        insert_query = "INSERT INTO your_table_name (column1, column2, ...) VALUES (%s, %s, ...)"
        values = (data['value1'], data['value2'], ...)  # Adjust according to your data structure
        cursor.execute(insert_query, values)
        connection.commit()
        
        calls_made += 1
        time.sleep(3600 / frequency)  # Sleep for the specified frequency (in seconds)

    # Close the database connection
    cursor.close()
    connection.close()

# Route to start the process of making REST calls and storing data
@app.route('/start_rest_calls', methods=['POST'])
def start_rest_calls():
    data = request.json
    endpoint = data.get('endpoint')
    frequency = data.get('frequency')
    duration = data.get('duration')

    # Start a new thread to make REST calls and store data asynchronously
    rest_thread = threading.Thread(target=make_rest_calls_and_store, args=(endpoint, frequency, duration))
    rest_thread.start()

    return jsonify({'message': 'REST calls and data storage started successfully'})

if __name__ == '__main__':
    app.run(debug=True)
