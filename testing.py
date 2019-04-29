from dotenv import load_dotenv
import requests
import json
import os
import pytest

CI_ENV = os.environ.get("CI", "OOPS") == "true"
SKIP_REASON = "to avoid issuing requests from the CI server"

load_dotenv()

app_id = os.environ.get("my_app_id", "Set an env variable named my_app_id")
app_key = os.environ.get("my_app_key", "Set an env variable named my_app_key")

@pytest.mark.skipif(CI_ENV==True, reason=SKIP_REASON)
def test_keys():
    url = f"https://api.edamam.com/search?q=chicken&app_id={app_id}&app_key={app_key}"
    search = requests.get(url)
    assert app_id != "Set an env variable named my_app_id"
    assert app_key != "Set an env variable named my_app_id"
    assert search.status_code == 200
