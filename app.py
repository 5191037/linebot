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
from argparse import ArgumentParser
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from flask import Flask
from flask_restful import Resource, Api
from pymongo import MongoClient
import json

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
