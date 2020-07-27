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
import os
import sys
import json

from argparse import ArgumentParser
from flask import Flask, request, abort
from flask_restful import Resource, Api

from pymongo import MongoClient

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, QuickReplyButton, MessageAction, QuickReply,
)

app = Flask(__name__)
api = Api(app)

# get channel_secret and channel_access_token from your environment variable
# channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
# channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
channel_secret = 'ccbef0158c3102cc91653b887bcd5101'
channel_access_token = '5aCn1mIzYby8URWx7i6bjxp8I0Egn9ptN7NhG8BbxZ+bqKPL7t6Dc6wLTRek4mOHPUKtyK2nDqHedeiMcs8ZQ42cCpTD7wA+y62epQ/G1N9W3O6cosz63nx3fwxJxUd6S0Lgbe7KcCj8c1MyludDAQdB04t89/1O/w1cDnyilFU='

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

    client = MongoClient('localhost', 27017)
    db = client.scraping
    collection = db.bot_fe

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        # return_text = ""
        # for record in collection.find(filter={'name': {'$regex': event.message.text}}):
        #     return_text += record["name"] + record["url"] + "\n"
        #
        # line_bot_api.reply_message(
        #     event.reply_token,
        #     TextSendMessage(text=return_text)
        # )

        if event.message.text == "攻略":
            hard_list = ["モバイルゲーム", "コンシューマーゲーム"]
            items = [QuickReplyButton(action=MessageAction(label=f"{hard}", text=f"{hard}")) for hard in hard_list]
            messages = TextSendMessage(text="ゲームのハードは？",quick_reply=QuickReply(items=items))
            line_bot_api.reply_message(event.reply_token, messages=messages)
        elif event.message.text == "モバイルゲーム":
            mobile_list = ["FGO攻略", "パズドラ攻略", "グラブル攻略", "遊戯王デュエルリンクス攻略", "ミラクルニキ攻略",
                           "陰陽師攻略", "ドッカンバトル攻略", "ウマ娘攻略", "ブラウンダスト攻略", "キンスレ攻略",
                           "ポケ森攻略", "モンハンライダーズ攻略", "ARK攻略", "リン攻略", "トラハ攻略",
                           "ラングリッサー攻略", "アイアンサーガ攻略", "アナムネシス攻略", "ツイステ攻略", "CODモバイル攻略",
                           "デュエマプレイス攻略", "AFKアリーナ攻略", "エンゲージソウルズ攻略", "ドラクエタクト攻略", "クレストリア攻略",
                           "エピックセブン攻略", "ポケットタウン攻略", "アルカラスト攻略", "アストロキングス攻略", "ラストエスケイプ攻略",
                           "脱出ゲーム攻略", "ダンジョンメーカー攻略", "オクトパストラベラー大陸の覇者攻略"]
            items = [QuickReplyButton(action=MessageAction(label=f"{mobile}", text=f"{mobile}")) for mobile in mobile_list]
            messages = TextSendMessage(text="探してるゲームは？",quick_reply=QuickReply(items=items))
            line_bot_api.reply_message(event.reply_token, messages=messages)
        elif event.message.text == "コンシューマーゲーム":
            consumer_list = ["艦これ攻略", "あつ森攻略", "ラストオブアス2攻略", "ゼノブレイドリマスター（DE）攻略", "ゴーストオブツシマ攻略",
                             "ドラゴンボールZカカロット攻略", "ニンジャラ（Ninjala）攻略", "グラブルVS攻略", "R6S攻略", "デスストランディング攻略",
                             "Dead by Daylight攻略", "ジャッジアイズ攻略", "RDR2攻略", "スパイダーマンPS4攻略", "PixARK攻略",
                             "オクトパストラベラー攻略", "二ノ国2攻略", "仁王2攻略", "ダークソウルリマスタード攻略", "SEKIRO攻略",
                             "聖剣伝説3攻略", "ドラクエ2攻略", "ドラクエ3攻略", "ドラクエ5攻略", "ドラクエ11S攻略",
                             "ドラクエビルダーズ2攻略", "マリオオデッセイ攻略", "マリオメーカー2攻略", "新サクラ大戦攻略", "moon攻略",
                             "ウィッチャー3攻略", "ペルソナ5R攻略", "ペルソナ5スクランブル攻略", "龍が如く極2攻略", "龍が如く3攻略",
                             "龍が如く4攻略", "龍が如く5攻略", "龍が如く7攻略", "北斗が如く攻略", "ポケモン剣盾攻略",
                             "バイオ7攻略", "バイオRE2攻略", "バイオRE3攻略", "キングダムハーツ3攻略", "FF7攻略",
                             "FF7リメイク攻略", "FF8攻略", "FF10攻略"]
            items = [QuickReplyButton(action=MessageAction(label=f"{consumer}", text=f"{consumer}")) for consumer in consumer_list]
            messages = TextSendMessage(text="探してるゲームは？",quick_reply=QuickReply(items=items))
            line_bot_api.reply_message(event.reply_token, messages=messages)

        return_text = ""
        for record in collection.find(filter={'name': {'$regex': event.message.text}}):
            return_text += record["name"] + record["url"] + "\n"

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=return_text)
    )

    return 'OK'


if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', type=int, default=8080, help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()

    app.run(debug=options.debug, port=options.port, host='0.0.0.0')
