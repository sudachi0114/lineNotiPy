import requests

def get_token() -> str:
    with open('./TOKEN', 'r') as f:
        return f.readline().rstrip("\n")


def main() -> None:
    URL = "https://notify-api.line.me/api/notify"
    token = get_token()
    headers = {"Authorization" : "Bearer "+ token}


    message = "message by python"
    payload = { 'message' : message }
    r = requests.post(URL, headers=headers, params=payload,)


if __name__ == "__main__":
    print("main")
    main()
