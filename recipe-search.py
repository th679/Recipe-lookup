from dotenv import load_dotenv
import requests
import json
import os
import tkinter
import datetime

load_dotenv()

#Initialize GUI

window = tkinter.Tk()


def search_button_click():
    #code to run search, adapted from Robo-Advisor Project
    global search_value, app_key, app_id, request_url, response, parsed_response, recipes
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
    #Error trapping
    if 'Error' in response.text:
        print("Could not find recipe with that term. Please try again")
        quit()

search_button = tkinter.Button(text="Search", command=search_button_click)


selected_recipes = []
ingredients = []

def add_recipe_click():
    selection = recipe_select.get(recipe_select.curselection())
    for recipe in recipes:
        if selection == recipe["recipe"]["label"]:
            ingredients.append(recipe["recipe"]["ingredientLines"])
    selected_recipes.append(selection)
    #add selections to ListBox
    selections.delete(0, 'end')
    i = 1
    for selection in selected_recipes:
        selections.insert(i, selection)
        i = i + 1


add_button = tkinter.Button(text="Add Recipe", command=add_recipe_click)

t = datetime.datetime.now()

def show_ingredients_click():
    print("----------------------------")
    print("GROCERY LIST FOR " + t.strftime("%Y-%m-%d"))
    print("----------------------------")
    for ingredient in ingredients:
        for x in range(len(ingredient)):
            print(ingredient[x])

def clear_selection_click():
    selection = selections.get(selections.curselection())
    #clear lists
    selected_recipes.remove(selection)
    for recipe in recipes:
        if selection == recipe["recipe"]["label"]:
            ingredients.remove(recipe["recipe"]["ingredientLines"])
    #clear ListBox
    selection2 = selections.curselection()
    selections.delete(selection2[0])


show_ingredients_button = tkinter.Button(text="Show Grocery List", command=show_ingredients_click)
clear_selection_button = tkinter.Button(text="Remove Selected Item", command=clear_selection_click)


search_label = tkinter.Label(text="Enter recipe name or key words here:")
entry_value = tkinter.StringVar()
search = tkinter.Entry(textvariable=entry_value)
search_label.pack()
search.pack()
search_button.pack()

recipe_select_label = tkinter.Label(text="Select a recipe you would like to add from the dropdown:")
recipe_select = tkinter.Listbox()
recipe_select.config(width=0)
recipe_select_label.pack()
recipe_select.pack()
add_button.pack()

Vscrollbar2 = tkinter.Scrollbar()
Vscrollbar2.pack(side=tkinter.RIGHT, fill=tkinter.Y)
selections_label = tkinter.Label(text="Your Added Recipes:")
selections = tkinter.Listbox()
Vscrollbar2.config(command=selections.yview)
selections.config(yscrollcommand=Vscrollbar2.set, width=0)
selections_label.pack()
selections.pack()

#scrollbar code adapted from http://www.java2s.com/Code/Python/GUI-Tk/ListBoxwithscrollBar.htm


clear_selection_button.pack()
show_ingredients_button.pack()


window.mainloop()

#https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/99ce7522557f0a9c8690e48ac95bcce0d528b380/notes/python/packages/tkinter.md

