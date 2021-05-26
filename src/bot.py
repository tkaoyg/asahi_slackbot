# slackbot.bot というモジュールから Bot クラスをインポート
from slackbot.bot import Bot

def main():
    bot = Bot()
    bot.run() # 変数botに対してrun()メソッドを使用

if __name__ == "__main__":
    print("bot start")
    main()
    