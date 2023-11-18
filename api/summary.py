import requests

post_url = "https://chatapi.pdfgear.com/pdf/getsummary"
def summarize(text):
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