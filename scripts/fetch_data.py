import pandas as pd
import requests

def fetch_data():
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)
    products = response.json()

    df = pd.DataFrame(products)
    df.to_csv('data/raw_data.csv', index=False)
    print("Fetched and saved raw data successfully!")

if __name__ == "__main__":
    fetch_data()
