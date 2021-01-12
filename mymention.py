import os
import requests
import sys
import json
import pprint
import re


SLACK_API_URL = "https://slack.com/api/conversations.history"
API_TOKEN = os.environ["BIRTHDAY_TOKEN"]




print(profile_text)

#自己紹介channelからテキストを取得
def profile_text():
    payload = {
        "channel": "CE6NDH4FQ",
        "token": API_TOKEN,
        "limit": 10,
    }
    response = requests.get(SLACK_API_URL, params=payload)