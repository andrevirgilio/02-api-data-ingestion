import requests
import pandas as pd
from datetime import datetime


def extract_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed. Status code: {response.status_code}")
        return None

def transform_users(users):
    df = pd.DataFrame(users)

    df = df[
        [
            "id",
            "name",
            "username",
            "email",
            "phone",
            "website"
        ]
    ]
    df["ingestion_date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    return df

def load_users(df):
    extraction_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"Extraction date: {extraction_date}")

    df.to_csv("users.csv", index=False)

    print("CSV file generated successfully")

users = extract_users()

if users:
    df = transform_users(users)

    print(f"Number of users retrieved: {len(df)}")

    load_users(df)