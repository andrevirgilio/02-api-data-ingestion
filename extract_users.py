import requests
import pandas as pd

response = requests.get("https://jsonplaceholder.typicode.com/users")

users = response.json()

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

df.to_csv("users.csv", index=False)

print("CSV file generated successfully")