import requests
import pandas as pd

def extract_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return pd.DataFrame(response.json()['results'])
    else:
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")
        return None

def transform_data(data):
    if data is not None:
        # Fill NaN values in 'bensin95_discount' with the corresponding values from 'bensin95'
        data['bensin95_discount'].fillna(data['bensin95'], inplace=True)
        # Fill NaN values in 'diesel_discount' with the corresponding values from 'diesel'
        data['diesel_discount'].fillna(data['diesel'], inplace=True)
    return data

def load_data(data):
    if data is not None:
      
        data.to_csv("petrol_data.csv", index=False)
        print("Data loaded successfully to petrol_data.csv")

if __name__ == "__main__":
    api_url = "https://apis.is/petrol"

    # Extract data
    extracted_data = extract_data(api_url)

    # Transform data
    petrol_data = transform_data(extracted_data)

    # Load data
    load_data(petrol_data)

    # Head of the transformed data
    if petrol_data is not None:
        print(petrol_data.head())