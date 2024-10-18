# ローカル環境での起動方法
#        PS C:\temp\pythonProject1\streamlit\CloudTech_Splint7> streamlit run app_splint7.py

# https://www.youtube.com/watch?v=4nsTce1Oce8&t=1696s


import streamlit as st
from PIL import Image

import requests
import json

import streamlit as st
import pandas as pd
import os

st.title('Cloud Tech Academy')
st.caption('スプリント7の演習です ver 0.941')

# image = Image.open('./data/cloudtechacademy_logo.png')
# st.image(image, width=200)

st.subheader('はじめに')

code = '''
演習の仕様は以下の通りです。
ユーザーからの口コミのテキスト、画像、メールアドレス、氏名の入力に基づき、受信した口コミは Amazon DynamoDB に保存され、口コミ内容は Amazon Comprehend による感情分析を行い、その結果に基づいてカスタマイズされたお礼メールを、Amazon SES を介してユーザーに自動送信します。
また、画像はプロモーション用として使用するため、不適切な内容が含まれていないか、Amazon Rekognition による事前チェックを行います。(現在工事中)
口コミの投稿は、API Gateway を用いた API として呼び出されます。API のレスポンスを早めるため、API では口コミと画像のアップロードのみを行い、その後の分析やメール送信は、Amazon SQS を介して実行される AWS Step Functions のステートマシーンにより実行されます。

なお、webアプリは、streamlit よりwebアプリを形成し、作成したREST APIをコールする(任意)
streamlit で利用する Python コードは、ローカルPCで開発し、Git Hub に登録することで、streamlit と連携が可能となる。
そのため、ローカル PC での開発にVSCode を用いることで、Git Hub経由で streamlit 上の Pythonコードをアップデートすることが可能となる。

参考
https://streamlit.io/
'''
# python言語用のシンタックスハイライトを表示する(コード上)
st.code(code, language='python')

# st.subheader('本サイトの構成')

# image = Image.open('./data/splint7_ensyou_kouseizu.png')
# st.image(image, width=1000)

# st.code(code, language='python')
