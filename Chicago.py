import requests
import json

# City of Chicago Crime Data API Endpoint
API_URL = "https://data.cityofchicago.org/resource/ijzp-q8t2.json"

# Optional Parameters: Fetch more data to analyze structure
params = {
    "$limit": 5,  # Fetch a few records to inspect all fields
    "$order": "date DESC",  # Get the most recent crimes
}

# Fetch data from the API
response = requests.get(API_URL, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    
    # Print the first record in a structured format
    print("Example Record (Full Data Fields):")
    print(json.dumps(data[0], indent=4))  # Pretty print JSON

    print("\n------ List of All Fields Available ------")
    for key in data[0].keys():
        print(f"- {key}")

else:
    print(f"Error: Unable to fetch data (Status Code: {response.status_code})")
