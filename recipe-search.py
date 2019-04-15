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
    recipe_select_label = tkinter.Label(text="Select a recipe you would like to add from the dropdown:")
    recipe_select = tkinter.Listbox()
    i = 1
    for recipe in recipe_list:
        recipe_select.insert(i, recipe)
        i = i + 1
    recipe_select_label.pack()
    recipe_select.pack()

search_button = tkinter.Button(text="Search", command=search_button_click)



search_label.pack()
search.pack()

search_button.pack()



window.mainloop()


