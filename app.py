# -*- coding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

from __future__ import unicode_literals
import sys

from argparse import ArgumentParser
from flask import Flask, request, abort
from flask_restful import Api

from pymongo import MongoClient

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    QuickReplyButton, MessageAction, QuickReply,
    CarouselColumn, CarouselTemplate, TemplateSendMessage,
    URITemplateAction,
)


app = Flask(__name__)
api = Api(app)

# get channel_secret and channel_access_token from your environment variable
# channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
# channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
channel_secret = 'ccbef0158c3102cc91653b887bcd5101'
channel_access_token = '5aCn1mIzYby8URWx7i6bjxp8I0Egn9ptN7NhG8BbxZ' \
                       '+bqKPL7t6Dc6wLTRek4mOHPUKtyK2nDqHedeiMcs8ZQ42cCpTD7wA+y62epQ' \
                       '/G1N9W3O6cosz63nx3fwxJxUd6S0Lgbe7KcCj8c1MyludDAQdB04t89/1O/w1cDnyilFU= '

if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        client = MongoClient('localhost', 27017)
        db = client.scraping
        collection = db.bot_fe

        if event.message.text == "Search":
            hard_list = ["五十音順", "シリーズ"]
            items = [QuickReplyButton(action=MessageAction(label=f"{hard}", text=f"{hard}")) for hard in hard_list]
            messages = TextSendMessage(text="検索開始", quick_reply=QuickReply(items=items))
            line_bot_api.reply_message(event.reply_token, messages=messages)
            continue

        if event.message.text == "五十音順":
            hard_list = ["ア行", "カ行", "サ行", "タ行", "ナ行",
                         "ハ行", "マ行", "ヤ行", "ラ行"]
            items = [QuickReplyButton(action=MessageAction(label=f"{hard}", text=f"{hard}")) for hard in hard_list]
            messages = TextSendMessage(text="頭文字で検索", quick_reply=QuickReply(items=items))
            line_bot_api.reply_message(event.reply_token, messages=messages)
            continue

        if event.message.text == "ア行":
            a_list = ["AFKアリーナ", "ARK", "あつ森", "ウィッチャー3", "ウマ娘",
                      "エピックセブン", "エンゲージソウルズ", "オクトパストラベラー大陸の覇者", "オクトパストラベラー", "陰陽師"]
            i = [QuickReplyButton(action=MessageAction(label=f"{mobile}", text=f"{mobile}")) for mobile in a_list]
            messages = TextSendMessage(text="ア行一覧", quick_reply=QuickReply(items=i))
            line_bot_api.reply_message(event.reply_token, messages=messages)
            continue

        if event.message.text == "カ行":
            k_list = ["艦これ", "キンスレ", "キングダムハーツ3", "クレストリア", "グラブル",
                      "グラブルVS", "CODモバイル", "ゴーストオブツシマ"]
            i = [QuickReplyButton(action=MessageAction(label=f"{consumer}", text=f"{consumer}")) for consumer in
                 k_list]
            messages = TextSendMessage(text="カ行一覧", quick_reply=QuickReply(items=i))
            line_bot_api.reply_message(event.reply_token, messages=messages)
            continue

        if event.message.text == "サ行":
            s_list = ["新サクラ大戦", "ジャッジアイズ", "スパイダーマンPS4", "聖剣伝説3", "SEKIRO",
                      "ゼノブレイドリマスター（DE）"]
            i = [QuickReplyButton(action=MessageAction(label=f"{mobile}", text=f"{mobile}")) for mobile in s_list]
            messages = TextSendMessage(text="サ行一覧", quick_reply=QuickReply(items=i))
            line_bot_api.reply_message(event.reply_token, messages=messages)
            continue

        if event.message.text == "タ行":
            t_list = ["ダークソウルリマスタード", "デスストランディング", "Dead by Daylight", "デュエマプレイス", "ドッカンバトル",
                      "ドラクエ5", "ドラクエ11S", "ドラクエビルダーズ2", "ドラクエタクト", "ドラゴンボールZカカロット"]
            i = [QuickReplyButton(action=MessageAction(label=f"{mobile}", text=f"{mobile}")) for mobile in t_list]
            messages = TextSendMessage(text="タ行一覧", quick_reply=QuickReply(items=i))
            line_bot_api.reply_message(event.reply_token, messages=messages)
            continue

        if event.message.text == "ナ行":
            n_list = ["ニーアリィンカーネション", "仁王2", "二ノ国2", "ニンジャラ（Ninjala）"]
            i = [QuickReplyButton(action=MessageAction(label=f"{mobile}", text=f"{mobile}")) for mobile in n_list]
            messages = TextSendMessage(text="ナ行一覧", quick_reply=QuickReply(items=i))
            line_bot_api.reply_message(event.reply_token, messages=messages)
            continue

        if event.message.text == "ハ行":
            h_list = ["パズドラ", "FF7リメイク", "FF8", "FF10", "バイオ7",
                      "バイオRE3", "ペルソナ5R", "ペルソナ5スクランブル", "ポケ森", "ポケモン剣盾"]
            i = [QuickReplyButton(action=MessageAction(label=f"{mobile}", text=f"{mobile}")) for mobile in h_list]
            messages = TextSendMessage(text="ハ行一覧", quick_reply=QuickReply(items=i))
            line_bot_api.reply_message(event.reply_token, messages=messages)
            continue

        if event.message.text == "マ行":
            m_list = ["マリオオデッセイ", "マリオメーカー2", "ミラクルニキ", "moon", "モンハンライダーズ"]
            i = [QuickReplyButton(action=MessageAction(label=f"{mobile}", text=f"{mobile}")) for mobile in m_list]
            messages = TextSendMessage(text="マ行一覧", quick_reply=QuickReply(items=i))
            line_bot_api.reply_message(event.reply_token, messages=messages)
            continue

        if event.message.text == "ヤ行":
            y_list = ["遊戯王デュエルリンクス"]
            i = [QuickReplyButton(action=MessageAction(label=f"{mobile}", text=f"{mobile}")) for mobile in y_list]
            messages = TextSendMessage(text="ヤ行一覧", quick_reply=QuickReply(items=i))
            line_bot_api.reply_message(event.reply_token, messages=messages)
            continue

        if event.message.text == "ラ行":
            r_list = ["ラストエスケイプ", "ラストオブアス2", "ラングリッサー", "龍が如く極2", "龍が如く3",
                      "龍が如く4", "龍が如く5", "龍が如く7", "R6S", "RDR2"]
            i = [QuickReplyButton(action=MessageAction(label=f"{mobile}", text=f"{mobile}")) for mobile in r_list]
            messages = TextSendMessage(text="ラ行一覧", quick_reply=QuickReply(items=i))
            line_bot_api.reply_message(event.reply_token, messages=messages)
            continue

        if event.message.text == "シリーズ":
            hard_list = ["オクトパストラベラー", "グラブル", "ドラクエ", "FF", "ペルソナ",
                         "マリオ", "龍が如く"]
            items = [QuickReplyButton(action=MessageAction(label=f"{hard}", text=f"{hard}")) for hard in hard_list]
            messages = TextSendMessage(text="シリーズで検索", quick_reply=QuickReply(items=items))
            line_bot_api.reply_message(event.reply_token, messages=messages)
            continue

        lst = []
        for record in collection.find(filter={'name': {'$regex': event.message.text}}):
            lst.append(record)
        if event.message.text != 'News':
            columns = [
                CarouselColumn(
                    thumbnail_image_url=column['image'],
                    title="神ゲー攻略",
                    text=column['name'],
                    actions=[
                        URITemplateAction(
                            label="サイトを見に行く",
                            uri=column['url'],
                        )
                    ]
                )
                for column in lst
            ]
        else:
            columns = [
                CarouselColumn(
                    thumbnail_image_url=column['image'].replace('\u3000', '%E3%80%80'),
                    title="神ゲー攻略",
                    text=column['name'],
                    actions=[
                        URITemplateAction(
                            label="サイトを見に行く",
                            uri=column['url'],
                        )
                    ]
                )
                for column in lst
            ]

        messages = TemplateSendMessage(
            alt_text="CarouselTemplate",
            template=CarouselTemplate(columns=columns),
        )
        line_bot_api.reply_message(event.reply_token, messages=messages)
        continue

    return 'OK'


if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', type=int, default=8080, help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()

    app.run(debug=options.debug, port=options.port, host='0.0.0.0')
