from dotenv import load_dotenv
import requests
import json
import csv
import os

load_dotenv()

app_key = os.environ.get("my_app_key")
app_id = os.environ.get("my_app_id")


request_url = f"https://api.edamam.com/search?q=chicken&app_id={app_id}&app_key={app_key}"
response = requests.get(request_url)
parsed_response = json.loads(response.text)

print(parsed_response)
