import requests


def get_response(conversation):
    url = "http://localhost:11434/api/chat"
    payload = {
        "model": "gemma3:12b",
        "messages": conversation,
        "stream": False,
    }

    try:
        res = requests.post(url, json=payload)

        return res.json()["message"]["content"].strip()
    except Exception as e:
        return f'Error: {e}'
