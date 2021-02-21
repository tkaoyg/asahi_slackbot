import os
API_TOKEN = os.environ["BOT_API_TOKEN"]

DEFAULT_REPLY = "リプライします" # 下記プラグインに該当しない場合の処理

PLUGINS = [
    "slackbot.plugins", # ライブラリに同梱されているモジュール
    "botmodule", # 自作モジュール botmodule.py
]