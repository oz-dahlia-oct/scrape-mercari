#!/usr/bin/env python
# coding: utf-8

"""

--- Google Chrome のバージョンが上がったときの対応 ---
1. Google Chrome のバージョンを控える（以下リンクで確認可）
   chrome://settings/help
2. 新しいドライバーをインストール
   a 次のインストール先サイトへ行く。
     インストール先
     https://chromedriver.chromium.org/downloads
   b 1.で控えたバージョンに最も近いバージョンをダウンロード  
3. dist/driver フォルダ内に新しいフォルダを作成し、chromedriver.exe を投函
4. conf.py の driver_path を 3. で作成したフォルダ名に書き換える

"""


try:
    from setting import S # 連続稼働テスト用
except:
    pass


class Conf:
    """
    設定用のクラス
    静的に利用する
    ※ 状況に応じて書き換える
    """

    try:
        account = S.account
    except:
        account = ''

    try:
        pw = S.pw
    except:
        pw = ''

    # distribution 用
    # Python の環境を持っている場合は dist は False とする
    # dist False とするばあい、pip install chromedriver-binary によるインストールが必要
    dist = False
    driver_path = './driver/9104472190/chromedriver'

    # 文字コード ( Windows であれば cp932、Mac であれば utf-8 とする )
    encoding = 'utf-8'

    # thread数
    thread_number = 3

    # 処理を途中から実行する場合
    from_the_middle = False  # 変更しない
    result_csv_name = None  # 変更しない

    # 実行内容を確認するために、ゆっくり動作させたい場合に使用。
    # 画面遷移ごとのスリープタイムを規定します（単位：秒）
    sleep_time = 0

    # 処理完了後にウィンドウを閉じずに待機する時間
    end_sleep = 0

