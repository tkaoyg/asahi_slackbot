from slackbot.bot import respond_to
from slackbot.bot import listen_to

# 「respond_to」メンションに応答
@respond_to("こんにちは")
def greeting_1(message):
    # Slackに応答を返す
    message.reply("こんにちは！")

# 「listen_to」はメンションがなくても特定の文字列の投稿があった際に応答する
@listen_to("あいうえお")
def greeting_2(message):
    message.reply("あいうえお　と入力されました")
    # message.react("melon") # メロン絵文字をリアクション