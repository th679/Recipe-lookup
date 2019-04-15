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
    #insert code to run search
    app_key = os.environ.get("my_app_key")
    app_id = os.environ.get("my_app_id")
    request_url = f"https://api.edamam.com/search?q=chicken&app_id={app_id}&app_key={app_key}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    print(parsed_response)

search_button = tkinter.Button(text="Search", command=search_button_click)





search_label.pack()
search.pack()

search_button.pack()

window.mainloop()

