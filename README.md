# Line Notify by python application 
python と LINE Notify を使って、python から LINE にメッセージを送ってみます。

## Using

* `venv`
* `requests`
* `LINE Notify`

## environment


### for the first time

```sh
python -m venv venv
```

### Use

```sh
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
```


## Usage:

* get LINE Notify Access Token like below.

```
.
├── README.md
├── TOKEN     # Put Access Token here (in text-file)
├── requirements.txt
└── src
    └── main.py
```

* execute (send message)

```sh
python src/main.py
```


### Access Token と URL の設定:

Access Token を含んだヘッダを作成

```python
API_URL = "https://notify-api.line.me/api/notify"
token = 'Your Access Token'
headers = {'Authorization': 'Bearer ' + token}
```


### メッセージを送信する:

`message` が空文字だと、LINE Notify からは何も送られてきません。
送信したいメッセージを `payload` に含めて、`requests.post` で送ることができます。

```python 
message = 'Hello LINE Notify!!'
payload = {'message': message}
r = requests.port(url=API_URL,
                  headers=headers,
                  params=payload)
```


### 画像を送信する:

画像は `files` という引数に含めて `requests.post` で送ります。

こちらも `message` が空文字だと、メッセージだけでなく、画像も送られてきません。

```python
message = 'Message with image!!
image = './path/to/image.png'  # You can chose [png] or [jpg]
payload = {'message': message}
files = {'imageFile': open(image, 'rb')}
r = requests.post(url=API_URL,
                  headers=headers,
                  params=payload,
                  files=files)
```


### スタンプを送信する:

スタンプを送信するには `stickerId` と `stickerPackageId` という2つの ID を指定する必要があります。

[各スタンプ (LINEが用意しているモノ) の2つのIDはここ](https://devdocs.line.me/files/sticker_list.pdf)から探すことができます。

試しに、`stickerId=14`, `stickerPackageId=1` のスタンプを送信してみます。

送信するには `payload` に2つのID を含めて `requests.post` で送信します。

```python
message = "message with LINE stamp"
payload = {'message': message,
           'stickerId': 14,
           'stickerPackageId': 1
}
r = requests.post(url=API_URL,
                  headers=headers,
                  params=payload)
```

### スタンプと画像を送信する

ちなみにですが、スタンプと画像を一緒に送信すると、`メッセージ -> スタンプ -> 画像` の順に届きます。

```python
message = "message with LINE stamp"
payload = {'message': message,
           'stickerId': 14,
           'stickerPackageId': 1
}
image = './path/to/image.png'  # You can chose [png] or [jpg]
files = {'imageFile': open(image, 'rb')}
r = requests.post(url=API_URL,
                  headers=headers,
                  params=payload,
                  files=files)
```

## Tips: LINE Notify Access Token の取得方法
[LINE Notify](https://notify-bot.line.me/my/) にアクセスします。

<img src="https://github.com/sudachi0114/lineNotiPy/blob/pictures/pictures/LINE_Notify_page.png" alt="" title="LINE Notify front page">

だいたい、こんな感じの画面にたどり着きます。

右上に「ログイン」する場所があるので、そこから LINE の ID でログインします。

<img src="https://github.com/sudachi0114/lineNotiPy/blob/pictures/pictures/login_LINE.png" alt="" title="LINE Login">

すると右上が「ログイン」から「ユーザ名」に変わるので、再度ここをクリックし、マイページにいきます。

<img src="https://github.com/sudachi0114/lineNotiPy/blob/pictures/pictures/mypage.png" alt="" title="LINE Login">

下の方にアクセストークンを発行できる場所があるので、そこからどのトークルームに属するかを選択してアクセストークンを発行すれば OK です。

<img src="https://github.com/sudachi0114/lineNotiPy/blob/pictures/pictures/gen_access_token.png" alt="" title="LINE Login">

あとは設計次第なのですが、環境変数に持たせてもよし、ファイルに保存して送信時に読み込ませるもよし、です。


## Links
* [LINE Notify](https://notify-bot.line.me/my/)
* [LINE Sticker ID list](https://devdocs.line.me/files/sticker_list.pdf)
* [pythonでLINENotify使ってみる](https://qiita.com/pontyo4/items/10aa0ba0a17aee19e88e)
* [PythonでLINEにメッセージを送る](https://qiita.com/moriita/items/5b199ac6b14ceaa4f7c9)
* [LINE Notify Bot](https://github.com/moritagit/LINENotifyBot)
