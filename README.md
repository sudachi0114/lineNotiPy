# Line Notify by python application 
python と LINE Notify を使って、python から LINE にメッセージを送ってみます。

## Using

* `venv`

## environment


### for the first time

```sh
python -m venv venv
```

### Use

```sh
source venv/bin/activate

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

## Links
* [LINE Notify](https://notify-bot.line.me/my/)
* [PythonでLINEにメッセージを送る](https://qiita.com/moriita/items/5b199ac6b14ceaa4f7c9)
