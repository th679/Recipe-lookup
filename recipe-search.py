from dotenv import load_dotenv
import requests
import json
import os
import tkinter

load_dotenv()

#Initialize GUI

window = tkinter.Tk()

search_label = tkinter.Label(text="Enter recipe name or key words here:")
entry_value = tkinter.StringVar()
search = tkinter.Entry(textvariable=entry_value)


def search_button_click():
    #code to run search
    search_value = entry_value.get()
    app_key = os.environ.get("my_app_key")
    app_id = os.environ.get("my_app_id")
    request_url = f"https://api.edamam.com/search?q={search_value}&app_id={app_id}&app_key={app_key}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    recipe_list = []
    recipes = parsed_response["hits"]
    for recipe in recipes:
        recipe_list.append(recipe["recipe"]["label"])
    #Add recipes to ListBox
    i = 1
    for recipe in recipe_list:
        recipe_select.insert(i, recipe)
        i = i + 1

search_button = tkinter.Button(text="Search", command=search_button_click)



selected_recipes = []
ingredients = []

def add_recipe_click():
    search_value = entry_value.get()
    app_key = os.environ.get("my_app_key")
    app_id = os.environ.get("my_app_id")
    request_url = f"https://api.edamam.com/search?q={search_value}&app_id={app_id}&app_key={app_key}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    recipes = parsed_response["hits"]
    selected_recipes.append(recipe_select.get(recipe_select.curselection()))
    selection = recipe_select.get(recipe_select.curselection())
    for recipe in recipes:
        if selection == recipe["recipe"]["label"]:
            ingredients.append(recipe["recipe"]["ingredientLines"])
    print(ingredients)
    print(selected_recipes)
    
add_button = tkinter.Button(text="Add Recipe", command=add_recipe_click)



search_label.pack()
search.pack()

recipe_select_label = tkinter.Label(text="Select a recipe you would like to add from the dropdown:")
recipe_select = tkinter.Listbox()
recipe_select_label.pack()
recipe_select.pack()

search_button.pack()
add_button.pack()


window.mainloop()


