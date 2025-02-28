import requests  # Import the requests library to make HTTP requests

# Define a function to fetch data from a given URL
def fetch_data(url):
    response = requests.get(url)  # Send a GET request to the URL
    if response.status_code == 200:  # Check if the response status code is 200 (OK)
        return response.text  # Return the response text (content of the webpage)
    else:
        return f"Error: {response.status_code}"  # Return an error message if the request fails

# Run this block only if the script is executed directly
if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos/1"  # Define a sample URL to fetch data from
    data = fetch_data(url)  # Call the fetch_data function with the URL
    print(data)  # Print the fetched data to the console
