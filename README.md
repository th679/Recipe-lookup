# Recipe-lookup

## Prerequisites

- Anaconda 3.7
- Python 3.7
- Pip

## Installation

Use Anaconda to create and activate a new virtual environment.
Install package dependencies:

```py
pip install -r requirements.txt
```

## Setup
Obtain an Edamam Recipe Search API Key: https://developer.edamam.com/edamam-recipe-api

Then, create a new file in the repository called ".env" and specify your App ID and App Key in the ".env" file:

```py
my_app_id = "123456"
my_app_key = "123456"
```

## Usage

Run the recommendation script:

```py
python app/recipe-search.py
```