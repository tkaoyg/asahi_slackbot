import requests # requestsライブラリをインポート
from bs4 import BeautifulSoup 

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
             AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100"

def get_html(url, params=None, headers=None):
    """ get_html
    url: スクレイピング先URL
    params=検索サイトのパラメータ
    """
    try:
        resp = requests.get(url, params=params, headers=headers) # module.method
        soup = BeautifulSoup(resp.text, "html.parser")
        return soup
    except:
        return None

def get_search_url(word, engine="google"):
    """ get_search_url
    word: 検索するワード
    engine: 使用する検索サイト
    """
    try:
        if engine == "google":

            # google検索
            search_url = "https://www.google.co.jp/search?"
            search_params = {"q": word} # 文字列検索を意味するパラメータ"q"
            search_headers = {"User-Agent": user_agent}

            # データ取得
            soup = get_html(search_url, search_params, search_headers) # 引数を関数に渡す
            if soup != None: # 検索できたとき 
                tags = soup.select(".yuRUbf > a")
                urls = [tag.get("href") for tag in tags]
                return urls
            else: # get_html関数で戻り値がNoneだったとき(検索でエラーになったとき)
                return None
    except:
        return None

try:
    result = get_search_url("python")
    if result != None:
        print(result)
    else:
        print("取得できませんでした")
except:
    print("エラー")