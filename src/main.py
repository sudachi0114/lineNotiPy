import requests

def get_token() -> str:
    with open('./TOKEN', 'r') as f:
        return f.readline().rstrip("\n")


class LINENotifyBot:
    API_URL = "https://notify-api.line.me/api/notify"

    def __init__(self, access_token):
        self.__headers = {'Authorization': 'Bearer ' + access_token}

    def send(self, message):
        payload = { 'message' : message }
        print("sending message to LINE...")
        r = requests.post(
            url=LINENotifyBot.API_URL,
            headers=self.__headers,
            data=payload)
        print("Done.")

    def send_with_image(self, message, image):
        payload = {'message': message}
        print("sending message (with image) to LINE...")
        files = {'imageFile': open(image, 'rb')}
        r = requests.post(
            url=LINENotifyBot.API_URL,
            headers=self.__headers,
            data=payload,
            files=files)
        print("Done.")

    def send_with_stamp(self, message, stickerId, stickerPackageId):
        payload = {'message': message,
		   'stickerId': stickerId,
		   'stickerPackageId': stickerPackageId
        }
        r = requests.post(
            url=LINENotifyBot.API_URL,
	    headers=self.__headers,
	    data=payload)


    def send_with_attachement(self, message, image, stickerId, stickerPackageId):
        payload = {'message': message,
		   'stickerId': stickerId,
		   'stickerPackageId': stickerPackageId
        }
        print("sending message (with image and stamp) to LINE...")
        files = {'imageFile': open(image, 'rb')}
        r = requests.post(
            url=LINENotifyBot.API_URL,
            headers=self.__headers,
            data=payload,
            files=files)
        print("Done.")

    
def main() -> None:
    token = get_token()
    bot = LINENotifyBot(access_token=token)
    # bot.send(message="")
    """
    bot.send_with_image(message="hoge",
                        image='./testimage.jpg')

    bot.send_with_stamp(message="message with stamp",
                        stickerId=14,
                        stickerPackageId=1)
    """
    bot.send_with_attachement(message="message with stamp",
                              image='./testimage.jpg',
                              stickerId=14,
                              stickerPackageId=1)


if __name__ == "__main__":
    main()
