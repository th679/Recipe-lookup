from dotenv import load_dotenv
import requests
import json
import os
import pytest

CI_ENV = os.environ.get("CI") == "true"
SKIP_REASON = "to avoid issuing requests from the CI server"

load_dotenv()

app_id = os.environ.get("my_app_id", "Set an env variable named my_app_id")
app_key = os.environ.get("my_app_key", "Set an env variable named my_app_key")

@pytest.mark.skipif(CI_ENV==True, reason=SKIP_REASON)
def test_keys():
    assert app_id != "Set an env variable named my_app_id"
    assert app_key != "Set an env variable named my_app_id"

def get_response(search_value):
    app_key = os.environ.get("my_app_key", "Set an env variable named my_app_id")
    app_id = os.environ.get("my_app_id", "Set an env variable named my_app_id")
    url = f"https://api.edamam.com/search?q={search_value}&app_id={app_id}&app_key={app_key}"
    response = requests.get(url)
    return json.loads(response.text)

@pytest.mark.skipif(CI_ENV==True, reason=SKIP_REASON)
def test_search():
    search_value = "chicken"
    parsed_response = get_response(search_value)
    recipes = parsed_response["hits"]
    assert isinstance(parsed_response, dict)
    assert recipes != []


#https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/travis-ci.md


