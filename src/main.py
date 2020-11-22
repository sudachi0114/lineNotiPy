import requests

def get_token() -> str:
    with open('./TOKEN', 'r') as f:
        return f.readline().rstrip("\n")


class LINENotifyBot:
    API_URL = "https://notify-api.line.me/api/notify"

    def __init__(self, access_token):
        self.__headers = {'Authorization' : 'Bearer ' + access_token}

    def send(self, message):
        payload = { 'message' : message }
        print("sending message to LINE...")
        r = requests.post(
            url=LINENotifyBot.API_URL,
            headers=self.__headers,
            data=payload,)
        print("Done.")


def main() -> None:
    token = get_token()
    bot = LINENotifyBot(access_token=token)
    bot.send(message="Hello LINE Notify!!")


if __name__ == "__main__":
    main()
