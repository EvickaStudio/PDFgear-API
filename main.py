# Reverse engineering pfdgear api in progress, 🤪
# This is just a really quick and dirty script to get the summary of a message, not really usable yet, but it's still pretty cool
# TODO: Add more ways to get content from a message, like maybe a 🐲
import requests
import json

post_url = "https://chatapi.pdfgear.com/pdf/getsummary"

# This function is used to get the summary of a message
# It's pretty simple, but it does the job
def get_summary(text):
    data = {
        "user": "",
        "messages": None,
        "pdf": {
            "fileName": "",
            "pageCount": 1,
            "pages": [
                {
                    "pageIndex": 1,
                    "content": text,
                }
            ],
        },
        "stream": True,
        "language": "de-DE",
    }

    lenght = len(data) # This gets the length of the data

    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Host": "chatapi.pdfgear.com",
        "Expect": "100-continue",
        "Connection": "Keep-Alive",
        "Content-Length": str(lenght), # This is the length of the data
    }

    response = requests.post(post_url, json=data, headers=headers)
    return response.text # This returns the text

# This function is used to format the text
# It's kinda complicated but it works
def format_text(text):
    # Format the text to a readable format
    formatted_sentence = ""
    text_lines = text.split("\n") # This splits the text into lines

    for line in text_lines:
        if line.strip() == "":
            continue # This skips the line if it's empty

        data = json.loads(line)
        if "t" in data:
            formatted_sentence += data["t"] # This adds the line to the formatted sentence

    formatted_sentence = (
        formatted_sentence.strip()
    )  # Remove leading and trailing spaces, this is really important
    return formatted_sentence

# This is the message we want to get the summary of
message = """
-Einteilung der Übungsgruppen wird morgen (6556.2023) während der Vorlesung freigeschaltet.
-Dies ist eine Kopie einer Mitteilung, die in Ma I (6, 6 WiSe 23/24) gepostet wurde.
"""

# This is where we call the functions, it's so 🔥
message = format_text(get_summary(message))

# # parse message from Zusammenfassung: to 1.
# message = message.split("Zusammenfassung:")[1].split("1. ")[1].split("2. ")[0]
# # remove all whitespace if its not only one
# message = " ".join(message.split())
print(message)