import time
import requests
import socket

# Function to check if a web service is available
def check_web_service():
    try:
        response = requests.get("http://app:3000/todos")
        if response.status_code == 200:
            print("Web service is running.")
        else:
            print(f"Web service returned status code {response.status_code}")
    except requests.ConnectionError:
        print("Web service is not reachable.")

# Function to check if MongoDB is available
def check_db_service():
    try:
        mongo_host = "mongo"
        mongo_port = 27017
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)  # 3-second timeout
        result = sock.connect_ex((mongo_host, mongo_port))
        if result == 0:
            print("MongoDB service is running.")
        else:
            print("MongoDB service is not reachable.")
        sock.close()
    except socket.error as e:
        print(f"Error connecting to MongoDB: {e}")

# Main loop to repeatedly check the services
while True:
    print("Checking services...")
    check_web_service()
    check_db_service()
    time.sleep(10)  # Wait for 10 seconds before the next check
