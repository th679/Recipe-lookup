# Recipe-lookup

## About

This program allows you to lookup recipes using an Edamam API and generate a grocery list using the selected recipes.

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

## Testing

To run automated tests run the following script:

```py
pytest
```

It is also recommended that you integrate your repository with a continuous integration (CI) platform to run the automated tests when the repository is updated. The recommended CI platform is the [Travis CI](https://travis-ci.org/) platform.